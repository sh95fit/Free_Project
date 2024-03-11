from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from sqlalchemy.orm import Session
from database.auth_connection import auth_db
from schemas.auth_schemas import UserCreate, Token, RefreshToken
from crud.auth_crud import create_user, get_existing_user, pwd_context, get_user

from typing import Optional
from starlette import status

import os
from dotenv import load_dotenv

import redis
import secrets

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
redis_client = redis.StrictRedis(
    host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


# 회원가입 라우터
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def user_create(_user_create: UserCreate, db: Session = Depends(auth_db)):
    user = get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    create_user(db=db, user_create=_user_create)


# 로그인 라우터
@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(auth_db)):
    # 계정(username)과 패스워드(password) 체크
    user = get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 계정 또는 패스워드입니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Access Token 만들기
    # data = {
    #     "sub": user.username,
    #     "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # }
    # access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    # 함수로 JWT 토큰 생성 부분 분리
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    # 리프레시 토큰 생성
    refresh_token = create_refresh_token()

    # 리프레시 토큰을 redis에 저장
    store_refresh_token(username=user.username, refresh_token=refresh_token)

    if is_token_expired(access_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="만료된 토큰",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "refresh_token": refresh_token,
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def is_token_expired(token: str, is_refresh_token: bool = False):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration = datetime.utcfromtimestamp(payload["exp"])
        if is_refresh_token:
            return datetime.utcnow() > expiration
        return False
    except jwt.ExpiredSignatureError:
        return True
    except jwt.JWTError:
        return True


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return username


# 토큰 유효성 검증 API 엔드포인트
@router.post("/validate-token")
async def validate_token(current_user: Optional[str] = Depends(get_current_user)):
    # 토큰이 검증되었을 때 유효한 응답 반환
    return {"valid": True}


# Refresh Token 처리 관련

# refresh token 저장
def store_refresh_token(username: str, refresh_token: str):
    # redis_key = f"refresh_token:{username}"
    # refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    # redis_client.setex(
    #     redis_key, int(refresh_token_expires.total_seconds()), refresh_token)
    redis_key = f"refresh_token:{refresh_token}"
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    redis_client.setex(
        redis_key, int(refresh_token_expires.total_seconds()), username)


def create_refresh_token():
    return secrets.token_urlsafe(32)


def verify_refresh_token(refresh_token: str) -> Optional[str]:
    # 리프레시 토큰 유효성 검사
    username = redis_client.get(f"refresh_token:{refresh_token}")

    return username if username else None


@router.post("/refresh-token")
async def refresh_access_token(refresh_token: RefreshToken):
    refresh_token = refresh_token.refresh_token
    username = verify_refresh_token(refresh_token)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="잘못된 리프레시 토큰",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if username:
        # 새로운 엑세스 토큰 생성
        new_access_token = create_access_token(
            data={"sub": username},
            expires_delta=access_token_expires
        )
        return {
            "access_token": new_access_token,
            "token_type": "bearer",
            "username": username,
            "refresh_token": refresh_token,
        }
    else:
        raise credentials_exception

from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from sqlalchemy.orm import Session
from database.auth_connection import auth_db
from schemas.auth_schemas import UserCreate, Token
from crud.auth_crud import create_user, get_existing_user, pwd_context, get_user

from starlette import status

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


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

    if is_token_expired(access_token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="만료된 토큰",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
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


def is_token_expired(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration = datetime.utcfromtimestamp(payload["exp"])
        return datetime.utcnow() > expiration
    except jwt.ExpiredSignatureError:
        return True
    except jwt.JWTError:
        return True

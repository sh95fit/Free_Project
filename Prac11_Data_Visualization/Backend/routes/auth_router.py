from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

from sqlalchemy.orm import Session
from database.auth_connection import auth_db
from schemas.auth_schemas import UserCreate
from crud.auth_crud import create_user, get_existing_user

from starlette import status

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# 로그인 테스트 툴


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# 회원가입 라우터
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: UserCreate, db: Session = Depends(auth_db)):
    user = get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    create_user(db=db, user_create=_user_create)

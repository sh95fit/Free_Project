from passlib.context import CryptContext
from sqlalchemy.orm import Session
# from database.session.auth_db import Session
from schemas.auth_schemas import UserCreate
from models.auth_models import User


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


# 회원가입
def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    db.commit()

# 중복값 예외 처리


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first

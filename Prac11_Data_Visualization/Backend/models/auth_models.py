from sqlalchemy import Column, String, Integer, Float, DateTime, func, select, VARCHAR, MetaData, Table, DECIMAL, text
from sqlalchemy.orm import declarative_base
from database.session.auth_db import engine, Auth_Base, Session
from pydantic import BaseModel


class User(Auth_Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(10), unique=True, nullable=False)
    password = Column(VARCHAR(10), nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)

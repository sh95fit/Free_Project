import pymysql

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import DATABASE_URL


engine = create_engine(DATABASE_URL)

SessionMain = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

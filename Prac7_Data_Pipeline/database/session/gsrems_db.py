import pymysql

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import GSREMS_URL

engine_gs = create_engine(GSREMS_URL)

SessionGsrems = sessionmaker(
    bind=engine_gs,
    autocommit=False,
    autoflush=False,
)

Base_gs = declarative_base()

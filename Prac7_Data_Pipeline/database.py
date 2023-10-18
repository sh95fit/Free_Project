import dotenv
import os
import pymysql

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

DATABASE_URL = f"mysql+pymysql://{os.environ['db_user']}:{os.environ['db_password']}@{os.environ['db_host']}:{os.environ['db_port']}/{os.environ['db_name']}"
# print(DATABASE_URL)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

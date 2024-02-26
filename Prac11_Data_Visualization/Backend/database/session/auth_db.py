from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import AUTH_DATABASE_URL

engine = create_engine(AUTH_DATABASE_URL)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Auth_Base = declarative_base()

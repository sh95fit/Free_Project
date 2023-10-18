from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(30), nullable=False)
    api_key = Column(String(100), nullable=False)
    create_date = Column(DateTime, nullable=False)

import os
from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI, WebSocket, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import asyncio
import pymysql
import logging

app = FastAPI()

load_dotenv()

config = dotenv_values(
    r"D:\Hun's\Hun's\sh95fit_git\Free_Project\Prac13_WebSocket\.env")

MYSQL_HOST = config['MYSQL_HOST']
MYSQL_PORT = config['MYSQL_PORT']
MYSQL_USER = config['MYSQL_USER']
MYSQL_PASSWORD = config['MYSQL_PASSWORD']
MYSQL_DB = config['MYSQL_DB']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 테이블 모델 정의
class Data(Base) :
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String(100), index=True)
    data = Column(String(300))

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 데이터베이스 연결 함수
def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터베이스에 데이터를 삽입하는 함수
def insert_data(db, ip, data):
    db.add(Data(ip=ip, data=data))
    db.commit()

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 웹 소켓 핸들러
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)) :
    await websocket.accept()
    ip = websocket.client.host

    logger.info(f"WebSocket connection established with {ip}")

    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received data from {ip}: {data}")
            # 받은 데이터를 MySQL에 삽입
            insert_data(db, ip, data)
    except Exception as e :
        logger.error(f"An error occurred: {str(e)}")

# WebSocket 클라이언트를 저장할 딕셔너리
clients = {}

# WebSocket 연결 핸들러
async def websocket_handler(websocket: WebSocket, db = Depends(get_db)):
    await websocket.accept()
    ip = websocket.client.host
    clients[ip] = websocket

    logger.info(f"WebSocket connection established with {ip}")

    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received data from {ip}: {data}")
            # 받은 데이터를 MySQL에 삽입
            insert_data(db, ip, data)
    except Exception as e:
        # 클라이언트가 연결을 종료하면 예외 처리
        del clients[ip]
        logger.error(f"An error occurred: {str(e)}")
        pass

# WebSocket endpoint 등록
app.add_websocket_route("/ws", websocket_handler)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

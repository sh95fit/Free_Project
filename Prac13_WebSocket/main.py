# import os
# from dotenv import dotenv_values, load_dotenv
# from fastapi import FastAPI, WebSocket, Depends
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# import asyncio
# import pymysql
# import logging

# app = FastAPI()

# load_dotenv()

# config = dotenv_values(
#     r"D:\Hun's\Hun's\sh95fit_git\Free_Project\Prac13_WebSocket\.env")

# MYSQL_HOST = config['MYSQL_HOST']
# MYSQL_PORT = config['MYSQL_PORT']
# MYSQL_USER = config['MYSQL_USER']
# MYSQL_PASSWORD = config['MYSQL_PASSWORD']
# MYSQL_DB = config['MYSQL_DB']

# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # 테이블 모델 정의
# class Data(Base) :
#     __tablename__ = "data"

#     id = Column(Integer, primary_key=True, index=True)
#     ip = Column(String(100), index=True)
#     data = Column(String(300))

# # 데이터베이스 테이블 생성
# Base.metadata.create_all(bind=engine)

# # 데이터베이스 연결 함수
# def get_db() :
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # 데이터베이스에 데이터를 삽입하는 함수
# def insert_data(db, ip, data):
#     db.add(Data(ip=ip, data=data))
#     db.commit()

# # 로깅 설정
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # 웹 소켓 핸들러
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)) :
#     await websocket.accept()
#     ip = websocket.client.host

#     logger.info(f"WebSocket connection established with {ip}")

#     try:
#         while True:
#             data = await websocket.receive_text()
#             logger.info(f"Received data from {ip}: {data}")
#             # 받은 데이터를 MySQL에 삽입
#             insert_data(db, ip, data)
#     except Exception as e :
#         logger.error(f"An error occurred: {str(e)}")

# # WebSocket 클라이언트를 저장할 딕셔너리
# clients = {}

# # WebSocket 연결 핸들러
# async def websocket_handler(websocket: WebSocket, db = Depends(get_db)):
#     await websocket.accept()
#     ip = websocket.client.host
#     clients[ip] = websocket

#     logger.info(f"WebSocket connection established with {ip}")

#     try:
#         while True:
#             data = await websocket.receive_text()
#             logger.info(f"Received data from {ip}: {data}")
#             # 받은 데이터를 MySQL에 삽입
#             insert_data(db, ip, data)
#     except Exception as e:
#         # 클라이언트가 연결을 종료하면 예외 처리
#         del clients[ip]
#         logger.error(f"An error occurred: {str(e)}")
#         pass

# # WebSocket endpoint 등록
# app.add_websocket_route("/ws", websocket_handler)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)


# =======================================================================================
# # 일반적인 소켓 통신
# import socket
# from dotenv import dotenv_values, load_dotenv
# import pymysql
# import logging


# load_dotenv()

# config = dotenv_values(
#     r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac13_WebSocket\.env")

# MYSQL_HOST = config['MYSQL_HOST']
# MYSQL_PORT = int(config['MYSQL_PORT'])  # MySQL 포트는 정수형으로 변환해야 합니다.
# MYSQL_USER = config['MYSQL_USER']
# MYSQL_PASSWORD = config['MYSQL_PASSWORD']
# MYSQL_DB = config['MYSQL_DB']

# # 로깅 설정
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # TCP/IP 서버 설정
# HOST = '0.0.0.0'  # 모든 IP에서 연결 허용
# PORT = 10025  # 사용할 포트 번호


# def save_to_database(ip, data):
#     try:
#         # MySQL 연결
#         conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT,
#                                user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
#         cursor = conn.cursor()

#         # 데이터 삽입 쿼리 실행
#         sql = "INSERT INTO data (ip, data) VALUES (%s, %s)"
#         cursor.execute(sql, (ip, data))

#         # 변경사항 커밋
#         conn.commit()

#         # 연결 종료
#         conn.close()
#     except Exception as e:
#         logger.error("Error saving to database: %s", e)


# def main():
#     # 소켓 생성
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         # 소켓 주소와 포트 바인딩
#         server_socket.bind((HOST, PORT))

#         # 연결 대기 상태로 전환
#         server_socket.listen()

#         logger.info("Server listening on port %d", PORT)

#         while True:
#             try:
#                 # 클라이언트 연결 대기
#                 client_socket, client_address = server_socket.accept()
#                 logger.info("Connected by %s", client_address)

#                 # 데이터 수신
#                 data = client_socket.recv(1024)
#                 if not data:
#                     continue  # 데이터가 없으면 다음 루프로 넘어감

#                 # IP 주소와 데이터 추출
#                 ip = client_address[0]  # 처음 10바이트를 IP 주소로 간주
#                 data = data.decode('utf-8')  # 나머지 데이터를 실제 데이터로 간주

#                 save_to_database(ip, data)

#                 logger.info("Data received from %s: %s", ip, data)

#                 # 연결 종료
#                 client_socket.close()

#             except Exception as e:
#                 logger.error("Error handling client data: %s", e)


# if __name__ == "__main__":
#     main()
# =======================================================================================
import asyncio
import socket
from dotenv import dotenv_values, load_dotenv
import pymysql
import logging

load_dotenv()

config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac13_WebSocket\.env")

MYSQL_HOST = config['MYSQL_HOST']
MYSQL_PORT = int(config['MYSQL_PORT'])  # MySQL 포트는 정수형으로 변환해야 합니다.
MYSQL_USER = config['MYSQL_USER']
MYSQL_PASSWORD = config['MYSQL_PASSWORD']
MYSQL_DB = config['MYSQL_DB']

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TCP/IP 서버 설정
HOST = '0.0.0.0'  # 모든 IP에서 연결 허용
PORT = 10025  # 사용할 포트 번호


def save_to_database(ip, data):
    try:
        # MySQL 연결
        conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT,
                               user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB)
        cursor = conn.cursor()

        # 데이터 삽입 쿼리 실행
        sql = "INSERT INTO data (ip, data) VALUES (%s, %s)"
        cursor.execute(sql, (ip, data))

        # 변경사항 커밋
        conn.commit()

        # 연결 종료
        conn.close()
    except Exception as e:
        logger.error("Error saving to database: %s", e)


async def handle_client(client_socket, client_address):
    try:
        logger.info("Connected by %s", client_address)

        # 데이터 수신
        data = await loop.sock_recv(client_socket, 1024)
        if not data:
            return  # 데이터가 없으면 종료

        # IP 주소와 데이터 추출
        ip = client_address[0]  # 클라이언트의 IP 주소
        data = data.decode('utf-8')  # 받은 데이터를 UTF-8 형식으로 디코딩

        save_to_database(ip, data)

        logger.info("Data received from %s: %s", ip, data)

    except Exception as e:
        logger.error("Error handling client data: %s", e)

    finally:
        client_socket.close()


async def main():
    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    logger.info("Server listening on port %d", PORT)

    while True:
        client_socket, client_address = await loop.sock_accept(server_socket)
        loop.create_task(handle_client(client_socket, client_address))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

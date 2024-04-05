# from fastapi import FastAPI, WebSocket, Request, BackgroundTasks
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient
# import paho.mqtt.client as mqtt
# from dotenv import dotenv_values, load_dotenv

# load_dotenv()

# # docker run -d --name mqtt-mongodb -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=1234 -p 27017:27017 mongo
# # docker run -d --name mqtt-broker -p 1883:1883 -p 9001:9001 mqtt-broker

# # MQTT Broker 및 FastAPI 설정
# config = dotenv_values(
#     r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\.env")
# app = FastAPI()
# templates = Jinja2Templates(
#     directory=r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\templates")

# # MongoDB 클라이언트 설정
# client = MongoClient(config['MONGO_URI'])
# db = client[config['MONGO_DB']]
# collection = db[config['MONGO_COLLECTION']]

# # MQTT 브로커 정보
# broker_address = config['MQTT_BROKER_ADDRESS']
# port = int(config['MQTT_BROKER_PORT'])
# topic = config['MQTT_TOPIC']

# # MQTT 클라이언트 설정
# mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


# def on_message(client, event, msg_id, message):
#     payload = message.payload.decode()
#     data = {
#         "topic": message.topic,
#         "inv": payload['inv'],
#         "ina": payload['ina'],
#         "inp": payload['inp']
#     }
#     collection.insert_one(data)


# # MQTT 클라이언트에 메세지 수신 콜백 함수 등록
# mqtt_client.on_message = on_message

# # MQTT 브로커 연결
# mqtt_client.connect(broker_address, port)

# # MQTT 클라이언트가 브로커의 특정 주제를 구독하도록 설정
# mqtt_client.subscribe(topic)


# # 백그라운드 작업 : MQTT 클라이언트 실행
# def run_mqtt_client():
#     mqtt_client.loop_forever()


# # 웹소켓 클라이언트 : 실시간 데이터 전송
# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     while True:
#         latest_data = collection.find_one(sort=[('_id', -1)])
#         if latest_data:
#             await ws.send_json(latest_data)

# # 홈페이지 렌더링


# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# # 백그라운드 작업 실행
# background_tasks = BackgroundTasks()
# background_tasks.add_task(run_mqtt_client)


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)


################################################################
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import threading
import uvicorn


load_dotenv()

# MQTT 브로커 주소
broker_address = "localhost"
# MQTT 브로커 포트
broker_port = 1883

config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\.env")

# MongoDB 연결
mongo_client = MongoClient(config['MONGO_URI'])
db = mongo_client[config['MONGO_DB']]
collection = db[config['MONGO_COLLECTION']]

# MQTT 클라이언트 생성
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# 연결이 설정될 때 실행되는 콜백 함수


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 연결이 설정되면 구독을 수행합니다.
    client.subscribe("topic/test")

# 메시지가 도착했을 때 실행되는 콜백 함수


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # MongoDB에 메시지 저장
    post_id = collection.insert_one(
        {"topic": msg.topic, "payload": msg.payload.decode("utf-8")}).inserted_id


# 콜백 함수 설정
client.on_connect = on_connect
client.on_message = on_message

# MQTT 브로커에 연결
client.connect(broker_address, broker_port, 60)

# # 메시지 루프를 시작합니다.
# client.loop_start()

# MQTT 클라이언트를 별도의 스레드에서 실행
mqtt_thread = threading.Thread(target=client.loop_start)
mqtt_thread.daemon = True  # 스레드가 메인 스레드와 함께 종료되도록 설정
mqtt_thread.start()


app = FastAPI()


# FastAPI 루트 경로에 대한 핸들러
@app.get("/")
async def read_root():
    # MongoDB에서 최신 메시지를 가져옴
    latest_message = collection.find_one(sort=[('_id', -1)])
    if latest_message:
        return {"message": latest_message['payload']}
    else:
        return {"message": "No message received yet."}


# 이 파일을 직접 실행할 때만 서버를 실행
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

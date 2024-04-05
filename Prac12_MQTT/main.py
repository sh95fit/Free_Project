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
from fastapi import FastAPI, WebSocket, Request, BackgroundTasks, WebSocketState
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import paho.mqtt.client as mqtt
from dotenv import dotenv_values, load_dotenv
import asyncio

load_dotenv()

# MQTT Broker 및 FastAPI 설정
config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\.env")
app = FastAPI()
templates = Jinja2Templates(
    directory=r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\templates")

# MongoDB 클라이언트 설정
client = MongoClient(config['MONGO_URI'])
db = client[config['MONGO_DB']]
collection = db[config['MONGO_COLLECTION']]

# MQTT 브로커 정보
broker_address = config['MQTT_BROKER_ADDRESS']
port = int(config['MQTT_BROKER_PORT'])
topic = config['MQTT_TOPIC']

# 웹소켓 클라이언트 목록
websocket_clients = set()


# 백그라운드 작업 : MQTT 클라이언트 실행
def run_mqtt_client():
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    def on_message(client, event, msg_id, message):
        payload = message.payload.decode()
        data = {
            "topic": message.topic,
            "inv": payload['inv'],
            "ina": payload['ina'],
            "inp": payload['inp']
        }
        collection.insert_one(data)

        # 데이터를 수신하면 모든 WebSocket 클라이언트에게 전송
        for ws in websocket_clients:
            asyncio.create_task(send_data_to_websocket(ws, data))

    # MQTT 클라이언트에 메세지 수신 콜백 함수 등록
    mqtt_client.on_message = on_message

    # MQTT 브로커 연결
    mqtt_client.connect(broker_address, port)

    # MQTT 클라이언트가 브로커의 특정 주제를 구독하도록 설정
    mqtt_client.subscribe(topic)

    # MQTT 클라이언트 실행
    mqtt_client.loop_forever()


async def send_data_to_websocket(ws, data):
    await ws.send_json(data)


# 웹소켓 클라이언트 : 실시간 데이터 전송
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    websocket_clients.add(ws)
    try:
        while True:
            # 연결이 끊어지면 루프 종료
            if ws.client_state != WebSocketState.CONNECTED:
                break
            await asyncio.sleep(0.1)
    finally:
        websocket_clients.remove(ws)


# 홈페이지 렌더링
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# 백그라운드 작업 실행
background_tasks = BackgroundTasks()
background_tasks.add_task(run_mqtt_client)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

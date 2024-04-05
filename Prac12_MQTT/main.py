from fastapi import FastAPI, WebSocket, BackgroundTasks, Request
from pymongo import MongoClient
import paho.mqtt.client as mqtt
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import dotenv_values

# MongoDB 클라이언트 설정
config = dotenv_values(".env")
client = MongoClient(config['MONGO_URI'])
db = client[config['MONGO_DB']]
collection = db[config['MONGO_COLLECTION']]

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# MQTT 브로커 정보
broker_address = config['MQTT_BROKER_ADDRESS']
port = int(config['MQTT_BROKER_PORT'])
topic = config['MQTT_TOPIC']

# MQTT 클라이언트 설정


def on_message(client, userdata, message):
    # MQTT 메시지 수신 시 실행되는 콜백 함수
    payload = message.payload.decode()
    data = {
        "topic": message.topic,
        "inv": payload['inv'],
        "ina": payload['ina'],
        "inp": payload['inp']
    }
    collection.insert_one(data)


mqtt_client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.on_message = on_message
mqtt_client.connect(broker_address, port)
mqtt_client.subscribe(topic)

# 백그라운드 작업: MQTT 클라이언트 실행


def run_mqtt_client():
    mqtt_client.loop_forever()


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        # MongoDB에서 최근 데이터 가져오기
        latest_data = collection.find_one(sort=[('_id', -1)])
        if latest_data:
            await ws.send_json(latest_data)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 백그라운드 작업 실행
background_tasks = BackgroundTasks()
background_tasks.add_task(run_mqtt_client)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

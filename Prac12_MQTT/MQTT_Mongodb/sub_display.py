# main.py
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import paho.mqtt.client as mqtt
from datetime import datetime
from dotenv import dotenv_values, load_dotenv
import threading
import asyncio
from queue import Queue
import logging
import websockets


app = FastAPI()

load_dotenv()

# # MQTT Broker 및 FastAPI 설정
config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\.env")

# MQTT 브로커 정보
broker_address = '127.0.0.1'
topic = config['MQTT_TOPIC']

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)


# 웹 소켓 연결 관리
connected_clients = set()

# MQTT 클라이언트 생성
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# MQTT 데이터 처리를 위한 큐
mqtt_data_queue = asyncio.Queue()

# MQTT 데이터 수신 시 호출되는 콜백 함수


def on_message(client, userdata, message):
    mqtt_data_queue.put_nowait(message.payload.decode())

# 웹 소켓 데이터 전송


async def send_websocket_data(websocket):
    while True:
        data = await mqtt_data_queue.get()
        await websocket.send_text(data)

# MQTT 데이터 수신 확인 함수


async def check_mqtt_data():
    while True:
        data = await mqtt_data_queue.get()
        for websocket in connected_clients:
            await websocket.send_text(data)

# 웹 소켓 엔드포인트


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(1)  # 웹 소켓 연결 유지
    except Exception as e:
        print(f"WebSocket connection error: {e}")
    finally:
        connected_clients.remove(websocket)

# 웹 페이지 엔드포인트


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <html>
            <head>
                <title>MQTT Data Monitoring</title>
            </head>
            <body>
                <h1>MQTT Data Monitoring</h1>
                <div id="data"></div>
                <script>
                    var ws = new WebSocket("ws://localhost:8000/");
                    ws.onmessage = function(event) {
                        document.getElementById("data").innerText = "Received message: " + event.data;
                    };
                </script>
            </body>
        </html>
    """

# 메인 함수


async def main():
    # MQTT 클라이언트 설정
    mqtt_client.on_message = on_message
    mqtt_client.connect(broker_address)
    mqtt_client.subscribe(topic)
    mqtt_client.loop_start()

    # 웹 소켓 서버 실행
    start_server = websockets.serve(send_websocket_data, "localhost", 8000)

    # 비동기 작업 실행
    await asyncio.gather(start_server, check_mqtt_data())

if __name__ == "__main__":
    asyncio.run(main())

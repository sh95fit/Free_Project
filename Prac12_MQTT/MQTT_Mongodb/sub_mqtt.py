import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient
from datetime import datetime
from dotenv import dotenv_values, load_dotenv
import logging

load_dotenv()

# # MQTT Broker 및 FastAPI 설정
config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\.env")

# # MongoDB 클라이언트 설정
client = MongoClient(config['MONGO_URI'])
db = client[config['MONGO_DB']]
collection = db[config['MONGO_COLLECTION']]

# MQTT 브로커 정보
broker_address = config['MQTT_BROKER_ADDRESS']
port = int(config['MQTT_BROKER_PORT'])
topic = config['MQTT_TOPIC']

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print("Received message: " + msg.payload.decode())
    # 받은 메시지를 JSON으로 파싱하여 MongoDB에 저장
    data = json.loads(msg.payload)
    # 현재 시간을 'save_time' 필드에 추가
    data['save_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    collection.insert_one(data)
    # print("Data saved to MongoDB")
    logger.info(datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S") + "   Data saved to MongoDB")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)

# 메시지를 받는 것을 계속해서 대기
client.loop_forever()

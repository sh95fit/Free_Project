import pika
import json
from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = dotenv_values(
    r"C:\Users\user\Desktop\KIMSEHUN\develop\Free_Project\Prac12_MQTT\MQTT_Mongodb\.env")

# MongoDB 클라이언트 설정
client = MongoClient(config['MONGO_URI'])
db = client[config['MONGO_DB']]
collection = db[config['MONGO_COLLECTION']]


# AMQP 브로커 정보
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 큐 생성
channel.queue_declare(queue='dev1')


def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Received message:", message)

    # MongoDB에 데이터 저장
    collection.insert_one(message)
    print("Data saved to MongoDB")


# 큐에 메시지가 도착할 때마다 callback 함수 호출
channel.basic_consume(
    queue='dev1', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')

# 메시지 수신 대기
channel.start_consuming()

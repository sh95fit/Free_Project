import pika
import json
import time

# AMQP 브로커 정보
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 큐 생성
channel.queue_declare(queue='dev1')

while True:
    # 데이터 생성
    data = {
        "inv": 123,
        "ina": 456,
        "outv": 789,
        "outp": 101
    }

    # 데이터를 JSON 형식으로 변환하여 발행
    channel.basic_publish(exchange='', routing_key='dev1',
                          body=json.dumps(data))

    # 터미널에 데이터 전송 여부 표시
    print("Data sent to AMQP broker")

    # 10초에 한 번씩 데이터 발행
    time.sleep(10)

# 연결 종료
connection.close()

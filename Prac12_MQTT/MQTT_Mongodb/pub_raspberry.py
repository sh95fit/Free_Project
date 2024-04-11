import paho.mqtt.client as mqtt
import json
import time

broker_address = "0.tcp.jp.ngrok.io"
port = 18531
topic = "dev1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 브로커에 연결
client.connect(broker_address, port)

while True:
    # 데이터 생성
    data = {
        "device_id": 1,
        "inv": 123,
        "ina": 456,
        "outv": 789,
        "outp": 101
    }

    # 데이터를 JSON 형식으로 변환하여 발행
    client.publish(topic, json.dumps(data))

    # 터미널에 데이터 전송 여부 표시
    print("Data sent to MQTT broker")

    # 10초에 한 번씩 데이터 발행
    time.sleep(10)

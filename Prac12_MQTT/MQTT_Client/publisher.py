# import paho.mqtt.client as mqtt
# import time

# # MQTT 브로커 정보
# broker_address = "127.0.0.1"  # 브로커의 IP 주소
# port = 1883  # MQTT 브로커의 포트
# topic = "dev1"  # 토픽 이름

# # MQTT 클라이언트 설정
# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# # MQTT 브로커에 연결
# client.connect(broker_address, port)

# # 메시지를 보낼 데이터
# data_to_send = {
#     "inv": 123,
#     "ina": 456,
#     "inp": 789
# }

# # 10초에 한 번씩 메시지를 보내는 루프
# while True:
#     # 보낼 메시지 생성
#     message = f"inv={data_to_send['inv']}, ina={data_to_send['ina']}, inp={data_to_send['inp']}"

#     # 토픽에 메시지 발행
#     client.publish(topic, message)

#     # 메시지 발행 정보 출력
#     print("Message sent:", message)

#     # 10초 대기
#     time.sleep(30)

# =============================================
import paho.mqtt.publish as publish

# MQTT 브로커 주소
broker_address = "localhost"
# MQTT 브로커 포트
broker_port = 1883

# MQTT 브로커에 메시지 발행
publish.single("topic/test", "MQTT",
               hostname=broker_address, port=broker_port)

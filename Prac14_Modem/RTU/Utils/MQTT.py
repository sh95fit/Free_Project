import paho.mqtt.client as mqtt
import json
from datetime import datetime
from dotenv import dotenv_values


class MQTT:
    def __init__(self, logger):
        self.logger = logger
        self.config = dotenv_values("/home/root/RTU/.env")

        self.broker_address = self.config['MQTT_BROKER_ADDRESS']
        self.port = int(self.config['MQTT_BROKER_PORT'])
        self.topic = self.config['MQTT_TOPIC']
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(self.broker_address, self.port)

    def sendData(self, req):
        #client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        #client.connect(self.broker_address, self.port)

        req = req.hex()

        if len(req) == 120:
            data = {
                "device_id": int(req[0:2], 16),
                "outar": int(req[8:12], 16)/10,
                "outas": int(req[12:16], 16)/10,
                "outat": int(req[16:20], 16)/10,
                "outvrs": int(req[20:24], 16),
                "outvst": int(req[24:28], 16),
                "outvtr": int(req[28:32], 16),
                "tpg": int(req[32:40], 16)/100,
                "operation": int(req[40:44], 16),
                "message": int(req[44:52], 16),
                "cpg": int(req[52:60], 16),
                "ina1": int(req[60:64], 16)/10,
                "inv1": int(req[64:68], 16),
                "ina2": int(req[68:72], 16)/10,
                "inv2": int(req[72:76], 16),
                "ina3": int(req[76:80], 16)/10,
                "inv3": int(req[80:84], 16),
                "ina4": int(req[84:88], 16)/10,
                "inv4": int(req[88:92], 16),
                "ina5": int(req[92:96], 16)/10,
                "inv5": int(req[96:100], 16),
                "ina6": int(req[100:104], 16)/10,
                "inv6": int(req[104:108], 16),
                "temp": int(req[108:112], 16),
                "fr": int(req[112:116], 16),
                "savetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(data)
        else:
            self.logger.error("[MQ] Data Length Incorrect...")

        # 데이터를 JSON 형식으로 변환하여 발행
        self.client.publish(self.topic, json.dumps(data))
        now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.logger.info(f"{now_date}[MQ] MQTT Success")

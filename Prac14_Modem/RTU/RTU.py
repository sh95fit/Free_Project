import os
import sys
import time
import datetime
import sched
import threading

from Utils.Logger import Logger
from Utils.MQTT import MQTT

from Configs.conf import Conf
from Inverter.Inverter import Inverter
from SerialManager import SerialManager


logDirectory = '/home/root/RTU/Logs'
logger = Logger(logDirectory, 'a')

conf = Conf()
mqtt = MQTT(logger)
serial = SerialManager(conf.rs485,logger)
inverter = Inverter(conf.rs485, logger)

if hasattr(conf, "rs485"):
    device = Inverter(conf.rs485, logger)
    print(device)
else:
    logger.error("Device Not Found...")
    raise ValueError


# 통신 포트 불러오기
port = serial.findBySerialPort()

# 인버터 유형 지정
inverter_type = input("Inverter Type DIP >> ").strip()

# 인버터 목록 가져오기
ivt_list = inverter.getSerialNumber(inverter_type)

# 인버터 데이터 가져오기
res = inverter.readData(inverter_type, port, ivt_list)

# 인버터 데이터 보내기
for r in res:
    mqtt.sendData(r)


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

if hasattr(conf, "rs485"):
    device = Inverter(conf.rs485, logger)
else:
    logger.error("Device Not Found...")
    raise ValueError


# 통신 포트 불러오기
port = SerialManager.findBySerialPort()
# 인버터 유형 지정
inverter_type = input().strip()

# 인버터 목록 가져오기
ivt_list = Inverter.getSerialNumber(inverter_type)

# 인버터 데이터 가져오기
res = Inverter.readData(inverter_type, port, ivt_list)

# 인버터 데이터 보내기
mqtt.sendData(res)

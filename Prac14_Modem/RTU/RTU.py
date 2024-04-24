import os
import sys
import time
import datetime
import sched
import threading

from Utils.Logger import Logger

from Configs.conf import Conf
from Inverter.Inverter import Inverter

Conf = Conf()
logDirectory = '/home/root/RTU/Logs'
logger = Logger(logDirectory, 'a')


if hasattr(Conf, "rs485"):
    device = Inverter(Conf.rs485, logger)
else:
    logger.error("Device Not Found...")

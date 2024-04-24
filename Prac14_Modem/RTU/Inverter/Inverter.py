from Inverter.DongYang import ESP25K
from SerialManager import SerialManager


class Inverter:
    def __init__(self, conf=None, logger=None):
        self.logger = logger
        self.conf = conf
        SerialManager(self.conf, self.logger)
        self.inverter = {
            "dip1": ESP25K.ESP_25K
        }

    def getSerialNumber(self, dip):
        ivt_list = []
        try:
            for i in range(100):
                req = self.inverter[dip].makeRequestData(i)
                port = SerialManager.findBySerialPort()
                # To Do
                # SerialManager Write 완성 및 데이터 없음(Null)이 아닐 경우 국번 추가
        except KeyboardInterrupt as e:
            self.logger.info(f"[IVT] Fource Quit... {e}")
            return ivt_list

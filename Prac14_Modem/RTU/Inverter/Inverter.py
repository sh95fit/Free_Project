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

        self.logger.info("[IVT] Find Serial Number ...")
        try:
            for i in range(100):
                req = self.inverter[dip].makeRequestData(i)
                port = SerialManager.findBySerialPort()
                # To Do
                # SerialManager Write 완성 및 데이터 없음(Null)이 아닐 경우 국번 추가
                if SerialManager.write(port, req):
                    ivt_list.append(i)
                else:
                    pass

            self.logger.info(f"[IVT] Valied Inverter : {ivt_list}")
            return ivt_list

        except KeyboardInterrupt as e:
            self.logger.info(f"[IVT] Force Quit... {e}")
            return ivt_list

    def readData(self, dip, port, ivt_list):
        res_list = []
        for ivt in ivt_list:
            self.logger.info(f"[IVT] Read Inverter {ivt} Data ...")
            req = self.inverter[dip].makeRequestData(ivt)

            res = SerialManager.write(port, req)
            res = str(ivt.zfill(2))+res

            if res:
                res_list.append(res)

        return res_list

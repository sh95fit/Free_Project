# 통신 타입 선택
import usb.core
import usb.util
import serial
import time
import serial.tools.list_ports


class SerialManager:
    def __init__(self, conf, logger):
        self.logger = logger
        self.conf = conf
        self.info = {
            "port": []
        }

    def init(self):
        self.info["port"] = []

    def find_usb_to_rs485(self, vendor_id, product_id):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.vid == vendor_id and port.pid == product_id:
                return port.device
        return None

    def findBySerialPort(self):
        self.init()
        self.logger.info("[SM] Find serial device by port ")
        vendor_id, product_id = list(map(int, self.conf['did'].split(':')))
        self.info["port"] = self.find_usb_to_rs485(vendor_id, product_id)

        if self.info["port"] != None:
            self.logger.info(f"[SM] USBtoRS485 Device Port:{self.info["port"]}")
        else:
            self.logger.error("[SM] USBtoRS485 Device Not Found...")
        return self.info["port"][0]

    def write(self, port, req):
        serial_com = serial.Serial(
            port=port,
            baudrate=self.conf['baudrate'],
            bytesize=self.conf['bytesize'],
            parity=self.conf['parity'],
            stopbits=self.conf['stopbits'],
            timeout=2
        )

        serial_com.write(bytes(bytearray(req)))
        time.sleep(0.1)
        res = serial_com.readline()

        return res

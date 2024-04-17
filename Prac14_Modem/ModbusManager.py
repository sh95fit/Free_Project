import serial
import time
from CRC16 import crc16

serial_port = "COM5"
baudrate = 9600
bytesize = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE

# 시리얼 포트 초기화
serial_com = serial.Serial(
    port=serial_port,
    baudrate=baudrate,
    bytesize=bytesize,
    parity=parity,
    stopbits=stopbits,
    timeout=2
)

size = 5
sop = 0x7e
write_command = 0x07
read_command = 0x08
send_command = 0x14
source = 0x01
type = 0x02  # 3상기준
error = {
    "none": 0x00,
    "open": 0x38,
    "get": 0x39
}
id = 0x01

# 요청 패킷
req = [sop, id, write_command]
req.extend(crc16(req))

print(req)

# serial_com.open()

serial_com.write(bytes(bytearray(req)))
time.sleep(0.1)
res = serial_com.readline()

print(res.hex())

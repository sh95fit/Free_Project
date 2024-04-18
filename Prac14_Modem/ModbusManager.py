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
time.sleep(0.05)
res = serial_com.readline()

print(res.hex())


def toNum(byte_arr, divider=1, temp=False, reverse=False):
    product = 1
    byte_arr = list(byte_arr)
    if (reverse):
        byte_arr.reverse()
    if (temp):
        if ((byte_arr[0] & 0xF0) > 0):
            product = -1
        byte_arr[0] = byte_arr[0] & 0x0F
    result = int.from_bytes(byte_arr, "big")
    return product*result/divider


result = {}


def convert(data):
    result["inv"] = int(data[10:14], 16)
    result["ina"] = int(data[14:18], 16)
    result["inp"] = int(data[18:26], 16)
    result["outvr"] = int(data[26:30], 16)
    result["outvs"] = int(data[30:34], 16)
    result["outvt"] = int(data[34:38], 16)
    result["outar"] = int(data[38:42], 16)
    result["outas"] = int(data[42:46], 16)
    result["outat"] = int(data[46:50], 16)
    result["outp"] = int(data[50:58], 16)
    result["pf"] = int(data[58:62], 16)/10
    result["frq"] = int(data[62:66], 16)/10
    result["cpg"] = int(data[66:82], 16)
    result['err'] = int(data[82:86], 16)

    return result


print(res.hex())
print(convert(res.hex()))

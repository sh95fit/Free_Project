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

id = 0x01

write_size = 8
write_function = 0x03
start_high = 0x75
start_row = 0x61
register_high = 0x00
register_row = 0x1b


# 요청 패킷
req = [id, write_function, start_high, start_row, register_high, register_row]
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
    result["outar"] = int(data[6:10], 16)/10
    result["outas"] = int(data[10:14], 16)/10
    result["outat"] = int(data[14:18], 16)/10
    result["outvrs"] = int(data[18:22], 16)
    result["outvst"] = int(data[22:26], 16)
    result["outvtr"] = int(data[26:30], 16)
    result["tpg"] = int(data[30:38], 16)/100
    result["operation"] = int(data[38:42], 16)
    result["message"] = int(data[42:50], 16)
    result["cpg"] = int(data[50:58], 16)
    result["ina1"] = int(data[58:62], 16)/10
    result["inv1"] = int(data[62:66], 16)
    result["ina2"] = int(data[66:70], 16)/10
    result['inv2'] = int(data[70:74], 16)
    result["ina3"] = int(data[74:78], 16)/10
    result['inv3'] = int(data[78:82], 16)
    result["ina4"] = int(data[82:86], 16)/10
    result['inv4'] = int(data[86:90], 16)
    result["ina5"] = int(data[90:94], 16)/10
    result['inv5'] = int(data[94:98], 16)
    result["ina6"] = int(data[98:102], 16)/10
    result['inv6'] = int(data[102:106], 16)
    result['temp'] = int(data[106:110], 16)/10
    result['fr'] = int(data[110:114], 16)/10

    return result


print(res.hex())
print(convert(res.hex()))

import usb.core
import usb.util
import serial
import time
import serial.tools.list_ports

from CRC16 import crc16

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)
time.sleep(0.1)
GPIO.output(23, GPIO.LOW)

VENDOR_ID = 0x0403
PRODUCT_ID = 0x6001

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None :
    raise ValueError('Device Not Found')


def find_usb_to_rs485():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.vid == 0x0403 and port.pid == 0x6001:
            return port.device
    return None

usbport = find_usb_to_rs485()

if usbport :
    print(f"USBtoRS485 Device Found... Port:{usbport}")
else :
    print("USBtoRS485 Device Not Found...")


serial_port = usbport
baudrate = 9600
bytesize = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE

serial_com = serial.Serial(
        port=serial_port,
        baudrate=baudrate,
        bytesize=bytesize,
        parity=parity,
        stopbits=stopbits,
        timeout=2
)


# Station Number
id = 0x01


# DongYang ESP25K Settings
size = 8
function = 0x03
start_high = 0x75
start_row = 0x61
register_high = 0x00
register_row = 0x1b


# Request Packet
req = [id, function, start_high, start_row, register_high, register_row]
req.extend(crc16(req))

print(req)


# Data Request
serial_com.write(bytes(bytearray(req)))
time.sleep(0.1)
res = serial_com.readline()
#print(res)
#res = res.hex()
check_res = res.hex()

#print(res)


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
    result["inv2"] = int(data[70:74], 16)
    result["ina3"] = int(data[74:78], 16)/10
    result["inv3"] = int(data[78:82], 16)
    result["ina4"] = int(data[82:86], 16)/10
    result["inv4"] = int(data[86:90], 16)
    result["ina5"] = int(data[90:94], 16)/10
    result["inv5"] = int(data[94:98], 16)
    result["ina6"] = int(data[98:102], 16)/10
    result["inv6"] = int(data[102:106], 16)
    result["inp"] = (result['inv1']*result['ina1']+
                     result['inv2']*result['ina2']+
                     result['inv3']*result['ina3']+
                     result['inv4']*result['ina4']+
                     result['inv5']*result['ina5']+
                     result['inv6']*result['ina6'])
    result["temp"] = int(data[106:110], 16)/10
    result["fr"] = int(data[110:114], 16)/10

    return result

# Data Length Error Handling
if len(res)>50:
    print(convert(check_res))


# Lora Connection
lora_port = "/dev/serial0"
lora_baudrate = 115200
lora_bytesize = serial.EIGHTBITS
lora_parity = serial.PARITY_NONE
lora_stopbits = serial.STOPBITS_ONE

lora_com = serial.Serial(
        port=lora_port,
        baudrate=lora_baudrate,
        bytesize=lora_bytesize,
        parity=lora_parity,
        stopbits=lora_stopbits,
        timeout=2
)


# Convert Data
def convert_to_byte_array(input_string):
    byte_array = []

    for char in input_string:
        ascii_value=ord(char)
        byte_array.append(int(hex(ascii_value),16))

    return byte_array

# Lora Command
send = [0x4C, 0x52, 0x57, 0x20, 0x34, 0x44, 0x20, 0x01, 0x01]
CRLF = [0x0D, 0x0A]

# real data
data = res[3:]

# test data
#data = res[6:71]

#print(data)

length = 0xFF&len(data)

#data = convert_to_byte_array(data)
#print(data)

# Make Command
send.append(length)
send.extend(data)
send.extend(CRLF)

send = bytes(bytearray(send))
print(send)

GPIO.output(23, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(23, GPIO.LOW)
lora_com.flushInput()
lora_com.flushOutput()
time.sleep(0.1)


lora_com.write(send)
time.sleep(0.1)
lora_result = lora_com.readline().strip().decode('utf-8')
print(lora_result)

lora_com.close()

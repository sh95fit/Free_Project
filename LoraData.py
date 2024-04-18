import serial
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT)
time.sleep(0.01)
GPIO.output(23, GPIO.LOW)

serial_port = "/dev/serial0"
baudrate = 115200
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

def convert_to_byte_array(input_string):
    byte_array = []

    for char in input_string:
        ascii_value=ord(char)
        byte_array.append(int(hex(ascii_value),16))
        #ascii_value=char
        #byte_array.append(int(ascii_value))

    return byte_array

send = [0x4C,0x52,0x57,0x20,0x34,0x44,0x20,0x01,0x01]


#command = "LRW 49\r\n"
command = [0x4C,0x52,0x57,0x20,0x34,0x39]
CRLF = [0x0D, 0x0A]

command.extend(CRLF)

command = bytes(bytearray(command))
print(command)
#time.sleep(10)


data = "11111"

length = 0xFF&len(data)
print(length)

data = convert_to_byte_array(data)

send.append(length)
print(data)

send.extend(data)
print(send)

send.extend(CRLF)
print(send)

send = bytes(bytearray(send))
print(send)
#serial_com.open()

GPIO.output(23, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(23, GPIO.LOW)

serial_com.write(send)
time.sleep(0.1)
send_data = serial_com.readline().strip().decode('utf-8')
print(send_data)
serial_com.close()



serial_com.open()
if serial_com.is_open:
    try:
        #serial_com.write(command.encode('utf-8'))
        serial_com.write(command)

        st_time = int(round(time.time()*1000))
        while True :
            GPIO.output(23, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(23, GPIO.LOW)

            #serial_com.write(command.encode('utf-8'))
            serial_com.write(command)
            
            time.sleep(0.1)
            en_time = int(round(time.time()*1000))
            print("Try")
            res = serial_com.readline().strip().decode('utf-8')
            #if serial_com.readline().strip().decode('utf-8') == "OK":
            if res == "OK":
                print(res)
                print("Connection Success")
                serial_com.close()
                break
            if st_time+30000 < en_time:
                print("Connection Failed")
                break

        serial_com.open()
        deveui = "LRW 3F\r\n"
        deveui = deveui.encode('utf-8')
        serial_com.write(deveui)
        st_time = int(round(time.time()*1000))

        while True:
            eui = serial_com.readline().strip().decode('utf-8')

            time.sleep(0.1)
            en_time = int(round(time.time()*1000))

            #print(eui)

            if eui :
                print(eui)
                serial_com.close()
                break
            if st_time+30000 < en_time:
                print("No received")
                break

        serial_com.open()
        appeui = "LRW 40\r\n"
        appeui = appeui.encode("utf-8")
        serial_com.write(appeui)
        time.sleep(0.1)
        appno = serial_com.readline().strip().decode('utf-8')
        print(appno)
        serial_com.close()


        serial_com.open()
        retx = "LRW 37 3\r\n"
        retx = retx.encode("utf-8")
        serial_com.write(retx)
        time.sleep(0.1)
        retxno = serial_com.readline().strip().decode('utf-8')
        print(retxno)
        serial_com.close()


    except serial.SerialException as e :
        print("Serial Exception : ", e)

    finally:
        #serial_com.close()
        pass
else :
    print("Failed to open serial port")

#time.sleep(10)
#data = "1234567890"
#data = convert_to_byte_array(data)
#print(data)
#send.extend(data)
#send.extend(CRLF)
#print(send)
#send = bytes(bytearray(send))
#print(send)
#serial_com.open()
#serial_com.write(send)
#time.sleep(0.1)
#send_data = serial_com.readline().strip().decode('utf-8')
#print(send_data)
#serial_com.close()



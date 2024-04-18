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

#command = "LRW 49\r\n"
command = [0x4C,0x52,0x57,0x20,0x34,0x39]
CRLF = [0x0D, 0x0A]

command.extend(CRLF)

command = bytes(bytearray(command))
print(command)

#serial_com.open()

if serial_com.is_open:
    try:
        #serial_com.write(command.encode('utf-8'))
        serial_com.write(command)

        st_time = int(round(time.time()*1000))
        while True :
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
                break
            if st_time+30000 < en_time:
                print("Connection Failed")
                break
            

        response = res

        print("Response : ", response)

    except serial.SerialException as e :
        print("Serial Exception : ", e)

    finally:
        #serial_com.close()
        pass
else :
    print("Failed to open serial port")

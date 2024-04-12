import serial
import time

serial_port = "/dev/serial1"
baudrate = 115200
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

# 시리얼 연결 확인 명령어
command = "LRW 49\r\n"

serial_com.open()

if serial_com.is_open():
    try:
        serial_com.write(command.encode('utf-8'))

        response = serial_com.readline().strip().decode('utf-8')

        print("Response : ", response)

    except serial.SerialException as e:
        print("Serial Exception : ", e)

    finally:
        serial_com.close()

else:
    print("Failed to open serial port.")

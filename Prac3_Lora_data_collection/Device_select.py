import DeviceID_Extraction as ID

check = 0
num = 0

#def select() :

while True :
    device_LTID = input("디바이스 LTID를 입력하세요 >>> ")

    if device_LTID not in ID.LTID :
        print("해당 디바이스가 존재하지 않습니다.")
    elif device_LTID in ID.LTID :
        num = ID.LTID.index(device_LTID)
        check = 1
        break
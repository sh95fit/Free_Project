import csv
import datetime
import time
import os
import Lora_Parser as LP
import DeviceID_Extraction as ID
import Device_select



def Data_save() :
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y%m%d")
    last_data = []
    now_data = []

    filename = "%s_%s.csv"%(nowDate, Device_select.device_LTID[8:])

#    raw_title =list(LP.res.keys())
    raw_title =list(LP.LE().keys())
    if not os.path.isfile("./Prac3_Lora_data_collection/"+filename) :
        f = open("./Prac3_Lora_data_collection/"+filename, 'a', newline='')
        writer = csv.writer(f)
        csvtitle = ['device-id']
        for i in raw_title :
            csvtitle.append(i)
        writer.writerow(csvtitle)

#        raw_data = list(LP.res.values())
        raw_data = list(LP.LE().values())
        now_data = raw_data[1:]
        raw_data.insert(0,ID.LTID[Device_select.num])
        writer.writerow(raw_data)
        f.close


    f = open("./Prac3_Lora_data_collection/"+filename, 'r')
    length = len(f.readlines())
    f.close

    if int(length) >= 2 :
        f = open("./Prac3_Lora_data_collection/"+filename, 'r')
        reader = csv.reader(f)
        last_data = list(reader)[-1]
        del last_data[3:5]
    #    last_data = (list(map(str,status[1:])))
    f.close

    nowtime = now.strftime("%H%M")

    while int(nowtime) <= 2000 :

        print(last_data[1:])
        print(now_data)

        if now_data != last_data[1:] :

            f = open("./Prac3_Lora_data_collection/"+filename, 'a', newline='')
            writer = csv.writer(f)

#            raw_data = list(LP.res.values())
            raw_data = list(LP.LE().values())
            raw_data.insert(0,ID.LTID[Device_select.num])

            writer.writerow(raw_data)

            del raw_data[2:4]
            last_data = list(map(str,raw_data))

            f.close
            print("%s시 데이터가 저장되었습니다."%(nowtime))

        time.sleep(30)
        now = datetime.datetime.now()
        nowtime = now.strftime("%H%M")

        raw_data = list(LP.LE().values())
        del raw_data[2:4]
        now_data = list(map(str,raw_data))
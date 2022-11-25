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


    filename = "%s_%s.csv"%(nowDate, Device_select.device_LTID[8:])

    raw_title =list(LP.res.keys())

    if not os.path.isfile("./Prac3_Lora_data_collection/"+filename) :
        f = open("./Prac3_Lora_data_collection/"+filename, 'a', newline='')
        writer = csv.writer(f)
        csvtitle = ['device-id']
        for i in raw_title :
            csvtitle.append(i)
        writer.writerow(csvtitle)

        f.close

    nowtime = now.strftime("%H%M")


    while int(nowtime) <= 2000 :
        f = open("./Prac3_Lora_data_collection/"+filename, 'a', newline='')
        writer = csv.writer(f)

        raw_data = list(LP.res.values())
        raw_data.insert(0,ID.LTID[Device_select.num])


        writer.writerow(raw_data)

        f.close

        time.sleep(60)
        now = datetime.datetime.now()
        nowtime = now.strftime("%H%M")
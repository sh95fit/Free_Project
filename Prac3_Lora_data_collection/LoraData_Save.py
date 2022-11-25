import csv
import datetime
import time
import os
import Lora_Parser as LP
import DeviceID_Extraction as ID

now = datetime.datetime.now()
nowDate = now.strftime("%Y%m%d")

filename = "%s.csv"%(nowDate)

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


while int(nowtime) <= 1039 :
    f = open("./Prac3_Lora_data_collection/"+filename, 'a', newline='')
    writer = csv.writer(f)

    raw_data = list(LP.res.values())
    raw_data.insert(0,ID.LTID[62])


    writer.writerow(raw_data)

    f.close

    time.sleep(60)
    now = datetime.datetime.now()
    nowtime = now.strftime("%H%M")
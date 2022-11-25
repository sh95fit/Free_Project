import csv
import datetime
import Device_select
import Lora_Parser as LP

now = datetime.datetime.now()
nowDate = now.strftime("%Y%m%d")


filename = "%s_%s.csv"%(nowDate, Device_select.device_LTID[8:])

f = open("./Prac3_Lora_data_collection/"+filename, 'r', newline='')

last_line = f.readlines()[-1]
last_line = last_line[24:]
last_line = last_line.replace(',','')
print(last_line)


now_line = list((LP.res.values()))

now_line = ''.join(map(str,now_line))
print(now_line)
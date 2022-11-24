import requests
import re
from Thingplug_info import Thingplug_info as info


# Lora 디바이스 검색 (API - searchMyDevice 활용)
division = "searchDevice"
function = "myDevice"
searchDevice_url = f"{info.ThingplugApiUrl}/{info.X_M2M_Origin}?division={division}&function={function}&startIndex=1&countPerPage=500"
#print(searchDevice_url)  
req = requests.get(searchDevice_url, headers=info.hdr)
data = re.findall('(?<=<device_Id>)(\w{0,})(?=<\/device_Id>)', req.text)

device_Id = []
for i in data :
    device_Id.append(i)

#print(device_Id)

LTID = []
for i in device_Id :
    LTID.append(str(info.App_EUI[1][8:])+i)
#print(LTID)
import requests
import re
import DeviceID_Extraction as ID
from Thingplug_info import Thingplug_info as info


# LTID 불러오기 확인
# print(ID.LTID)
#print(ID.LTID.index("0000068740ca63fffe102995"))
print(ID.LTID.index("00000687702c1ffffe5be270"))
#print(ID.LTID[3])

# Lora의 특정 디바이스 데이터 불러오기  (contentInstanceRetrieve 활용)
CIR_url = f"{info.ThingplugApiUrl}/{info.App_EUI}/{info.version}/remoteCSE-{ID.LTID[62]}/container-{info.container}/latest"
#print(CIR_url)
req = requests.get(CIR_url, headers = info.hdr)


if str(req.status_code) == '200' :
    data = re.findall('(?<=<con>)\w{0,}(?=<\/con>)', req.text)
#    print(data[0])
#    print(len(data[0]))

#req = requests.get("https://thingplugpf.sktiot.com:9443/0060231000000687/v1_0/remoteCSE-0000068740ca63fffe102995/container-LoRa/latest", headers = info.hdr)
#print(req)

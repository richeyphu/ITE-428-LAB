# ExtraPractice1.py

import requests
import json  # list , dictionary

url = "https://data.go.th/dataset/9bccd66e-8b14-414d-93d5-da044569350c/resource/70e1ac97-edfe-4751-8965-6bbe16fb21b4/download/data_station.json"
r = requests.get(url)
myData = json.loads(r.content)

# print("{}".format(myData))
# print("{}".format(type(myData)))

print("พบจำนวนสถานีรถไฟ {} รายการ".format(len(myData)))
for i in myData:
    print("\n{} {}".format(i["station_code"], i["name"]))
    print("{:>5}{} / {}".format("", i["en_name"], i["chname"]))
    if i["lat"] != 0 and i["long"] != 0:
        print("{:>6}{} , {})".format("(", i["lat"], i["long"]))

# ExtraPractice3.py

import requests
import json  # list , dictionary

url = "https://data.go.th/dataset/ee189de7-7131-4808-8c69-de101c0bd0e4/resource/7dcc70f4-b03d-4cdd-b2ce-d0b5fc66b91e/download/train_station.json"
r = requests.get(url)
data = json.loads(r.content)

# ['properties']['type'] = 1 -> ซื้อตั๋วบนสถานีได้

print("-" * 30)
print("สถานีรถไฟที่สามารถซื้อตั๋วบนสถานีรถไฟได้")
print("-" * 30)
n = 0
for i in data["features"]:
    n += 1
    tel = i["properties"]["tel"]
    # if tel == "-" or tel == "":
    #     tel = "ไม่มี"
    print("{:>2}.) {}\n{:>13} {}".format(n, i["properties"]["name"], "เบอร์โทร",
                                         tel if tel == "-" or tel == "" else "ไม่มี"))

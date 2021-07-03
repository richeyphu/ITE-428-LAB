# ExtraPractice2.py

import requests
import json  # list , dictionary

url = "https://data.go.th/dataset/84954e4a-3302-4b05-9dfc-c636f30b62ab/resource/31ddd8a7-c99a-43eb-8c2e-9644ddb1608b/download/university.json"
r = requests.get(url)
data = json.loads(r.content)

# print("{}".format(myData))
# print("{}".format(type(myData)))
# ['properties']['type'] = 3 = เอกชน

print("-" * 30)
print("สถาบันอุดมศึกษาเอกชน")
print("-" * 30)
n = 0
for i in data["features"]:
    if i["properties"]["type"] == "3":
        n += 1
        print("{}.) {} {}".format(n, i["properties"]["name"], i["properties"]["web"]))

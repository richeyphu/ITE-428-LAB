# ExtraPractice4.py
# สร้างรายงานเคส โควิด-19 ในแต่ละประเทศ

import requests
import json  # list , dictionary


def line():
    print("=" * 80)


def line2():
    print("-" * 80)


# นับจำนวนเคสและจำนวนผู้เสียชีวิตในแต่ละประเทศ และคืนค่าเป็น dict ใหม่
def dict_count_cases(c_set):
    c_stat = []
    l = len(c_set)
    for n, c in enumerate(c_set):
        # แสดง Loading Bar
        loading_bar(n, l)

        c_cases = 0
        c_deaths = 0
        name = ""
        # code = ""
        for j in data["records"]:
            if j["countriesAndTerritories"] == c:
                c_cases += j["cases"]
                c_deaths += j["deaths"]
                name = j["countriesAndTerritories"]
                # code = j["geoId"]
        # c_stat.append({"country": name, "code": code, "cases": c_cases, "deaths": c_deaths})
        c_stat.append({"country": name, "cases": c_cases, "deaths": c_deaths})
    return c_stat


def loading_bar(n, l):
    print("\rLoading Data : {} ({:.2f}%)".format("█" * round(n / l * 100 / 2), n / l * 100), end="")


def title():
    line()
    print("{:>48}".format("COVID-19 REPORT"))
    print("{:>54}".format("(" + min(alldate) + ") - (" + max(alldate) + ")"))
    line()
    print("\t  {}{:>32} {:>15}".format("Countries & Territories", "Cases", "Deaths"))
    line2()


# Online file ver.
url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
r = requests.get(url)
data = json.loads(r.content)

# # Local file ver.
# # Opening JSON file
# f = open("covid19_casedistribution.json", encoding="UTF-8")
# # returns JSON object as a dictionary
# data = json.load(f)

countries = set()
alldate = set()
for i in data["records"]:
    # จัดกลุ่มประเทศจาก JSON
    countries.add(i["countriesAndTerritories"])
    # จัดกลุ่มวันที่จาก JSON
    alldate.add("{}/{}/{}".format(i["year"], i["month"], i["day"]))

# แสดง Title
title()

# เรียงลำดับประเทศที่มี case มากที่สุดไปหาน้อยที่สุด
c_stat_numorder = sorted(dict_count_cases(countries), key=lambda k: k["cases"], reverse=True)

# ลบ Loading Bar
print("\r", end="")

all_cases = 0
all_deaths = 0
for i, v in enumerate(c_stat_numorder):
    all_cases += v["cases"]
    all_deaths += v["deaths"]
    # แสดงผล
    print("{:>3}.) {:<45}{:>10,} {:>15,}".format(i + 1, v["country"], v["cases"], v["deaths"]))
line2()
print("\t  TOTAL {:>49,} {:>15,}".format(all_cases, all_deaths))
line()

# แสดงกราฟเทียบอัตราส่วนจำนวนเคสทั่วโลกต่อจำนวนเคสแต่ละประเทศ
print("\t\t\t\t\t\t\t\tData Visualization")
line()
sum_percent = 0
for i, v in enumerate(c_stat_numorder):
    percent = round(v["cases"] / all_cases * 100, 2)
    if percent > 0.8:
        sum_percent += percent
        bar = "█" * round(percent)
        print("{:>3}.) {:<30} {} ({:.2f}%)".format(i + 1, v["country"], bar, percent))
other_percent = round(100 - sum_percent, 2)
print("\t  {:<30} {} ({:.2f}%)".format("OTHERS", "█" * round(other_percent), other_percent))
line()

# Closing file
# f.close()

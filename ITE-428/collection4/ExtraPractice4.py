# ExtraPractice4.py
# สร้างรายงานเคส โควิด-19 ในแต่ละประเทศ

import requests
import json  # list , dictionary
from os import path
from time import sleep
import threading


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
        loading_bar(n + 1, l)

        c_cases = 0
        c_deaths = 0
        name = ""
        # code = ""
        found = False
        for j in data["records"]:
            if j["countriesAndTerritories"] == c:
                c_cases += j["cases"]
                c_deaths += j["deaths"]
                name = j["countriesAndTerritories"]
                # code = j["geoId"]
                found = True
                continue
            if found:
                break
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


def clear_line():
    print("\r", end="")


# Online file ver.
def get_online_json():
    thr = threading.Thread(target=scrolling_text, args=("Connecting to Server " + "█ " * 20, 80))
    thr.start()
    # print("Connecting to server...", end="")

    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    r = requests.get(url)
    return json.loads(r.content)


# Local file ver.
def get_local_json():
    # Opening JSON file
    with open("covid19_casedistribution.json", encoding="UTF-8") as f:
        return json.load(f)  # returns JSON object as a dictionary


def scrolling_text(msg, n_chars):
    # """
    # Displays scrolling text of whatever 'msg' and ensures that only n_chars
    # are shown at a time. If n_chars is greater than the length of msg, then
    # the string displayed may "loop" around.
    #
    # Inputs:
    #     msg: str - The message to display
    #     n_chars: int - The number of characters to display at a time
    #
    # Outputs: Returns None, displays the scrolling text indefinitely.
    # """
    len_msg = len(msg)
    counter = 0
    while True:
        displayed = ""
        for char in range(n_chars):
            displayed += msg[(counter + char) % len_msg]
        print(f"\r{displayed}", end="")
        sleep(0.05)
        counter = (counter + 1) % len_msg

        # Check if loading done...
        global stop_threads
        if stop_threads:
            break


def get_countries_and_date(d):
    ct = set()
    ad = set()
    for i in d["records"]:
        # จัดกลุ่มประเทศจาก JSON
        ct.add(i["countriesAndTerritories"])
        # จัดกลุ่มวันที่จาก JSON
        ad.add("{}/{}/{}".format(i["year"], i["month"], i["day"]))
    return ct, ad


if __name__ == '__main__':
    stop_threads = False
    # Get JSON file
    data = get_local_json() if path.isfile("covid19_casedistribution.json") else get_online_json()
    stop_threads = True
    clear_line()

    # Get countries and date set data
    countries, alldate = get_countries_and_date(data)

    # แสดง Title
    title()

    # เรียงลำดับประเทศที่มี case มากที่สุดไปหาน้อยที่สุด
    c_stat_numorder = sorted(dict_count_cases(countries), key=lambda k: k["cases"], reverse=True)

    # ลบ Loading Bar
    clear_line()

    all_cases = 0
    all_deaths = 0
    for i, v in enumerate(c_stat_numorder):
        all_cases += v["cases"]
        all_deaths += v["deaths"]
        # แสดงผล
        print("{:>3}.) {:<45}{:>10,} {:>15,}".format(i + 1, v["country"].replace('_', ' '), v["cases"], v["deaths"]))
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
            print("{:>3}.) {:<30} {} ({:.2f}%)".format(i + 1, v["country"].replace('_', ' '), bar, percent))
    other_percent = round(100 - sum_percent, 2)
    print("\t  {:<30} {} ({:.2f}%)".format("OTHERS", "█" * round(other_percent), other_percent))
    line()

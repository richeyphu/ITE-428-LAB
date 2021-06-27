# function declaration
import math


def line1():
    print("-" * 35)


def line2(ch):  # line2('#')
    # print(ch * 35)
    print("{}".format(ch) * 35)


def line3(ch, num):
    print("{}".format(ch) * num)


def calBMI(w, h):
    bmi = w / math.pow(h, 2)
    return bmi


def create_email(name, last):
    return "{}.{}_st@tni.ac.th".format(last[0:2].lower(), name.lower())

# if, comparison operator

# Slide p.91
import math


def line():
    print("*" * 50)


def cal_circle_area(r):
    return math.pi * (r ** 2)


def cal_rectangle_area(w, l):
    return w * l


line()
print("{:>27}".format("MENU"))
line()
print("C or c  Area of Circle")
print("S or S  Area of Rectangle")
line()
choice = input("Enter Your Choice : ").lower()
line()

if choice == 'c':
    radius = float(input("Please Input Radius : "))
    area = cal_circle_area(radius)
elif choice == 's':
    width = float(input("Please Input Width : "))
    length = float(input("Please Input Length : "))
    area = cal_rectangle_area(width, length)
else:
    print("ERROR: Invalid Choice")
    exit()

line()
print("AREA = {:.2f}".format(area))
line()

# BMI Calculation

import math
import datetime
import pymongo
from MyLibrary import line3, calBMI


print("Calculating BMI")
height = float(input("Enter your height in centimeter : "))
weight = float(input("Enter your weight in kilogram   : "))
heightM = height / 100

# BMI = weight / (heightM ** 2)
# BMI = weight / math.pow(heightM, 2)
BMI = calBMI(weight, heightM)

line3('*', 20)
print("Your BMI is {:.2f}".format(BMI))
line3('%', 50)

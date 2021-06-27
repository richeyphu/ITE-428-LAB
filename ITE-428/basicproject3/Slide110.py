# Slide p.110
def line():
    print("*" * 70)


price = float(input("Input price of car : "))
dep = float(input("Input depreciation per year (%) : "))
year = float(input("Input How many year you want to see : ")).__floor__()

line()
print("Price of Car = {:,.2f} BAHT".format(price))
line()

for i in range(1, year + 1):
    reduce = price * 5 / 100
    price -= reduce
    print("After use {} Year : Reduce = {:,.2f} BAHT\tPrice = {:,.2f} BAHT".format(i, reduce, round(price, 2)))

line()

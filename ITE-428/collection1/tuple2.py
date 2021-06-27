# tuple
def calvatAndTotal(price):
    vat = price * 7 / 100
    total = price + vat
    return vat, total


data = calvatAndTotal(100)
VAT = data[0]
TOT = data[1]
print("VAT = {}".format(VAT))
print("{}".format(data))
print("{}".format(type(data)))

V, T = calvatAndTotal(1500)
print("VAT   = {}".format(V))
print("TOTAL = {}".format(T))

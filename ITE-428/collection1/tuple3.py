# print("Adisak", "Suasaming", "Thai-nichi", sep="*")

# def calWeight(*dataweight):
#     sum = 0
#     for i in dataweight:
#         sum += i
#     avg = sum / len(dataweight)
#     return avg, sum


def calWeight(*dataweight, unit=""):
    # print("{}".format(type(dataweight)))
    sum1 = sum(dataweight)
    avg = sum1 / len(dataweight)
    avgWithUnit = "{:,.2f} {}".format(avg, unit)
    sumWithUnit = "{:,.2f} {}".format(sum1, unit)
    return avg, sum1, avgWithUnit, sumWithUnit


A, S, AU, SU = calWeight(78, 34, 56, 23, unit="kg")
print("{} -- {}".format(A, S))
print("{} -- {}".format(AU, SU))

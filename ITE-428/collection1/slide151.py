def checkNumber(*data, see=""):
    if see == "max-min":
        return max(data), min(data)
    elif see == "ab-bl-av":
        return count_avg(data)
    return


def count_avg(data):
    avg = sum(data) / len(data)
    a = b = 0
    for i in data:
        if i > avg:
            a += 1
        elif i < avg:
            b += 1
    return a, b


x, y = checkNumber(17, 22, 35, 55, 67, 38, 98, 109, 10, 5, 77, see="max-min")
print("MAXIMUM = {0}\nMINIMUM = {1}".format(x, y))
x, y = checkNumber(12, 99, 34, 67, 21, 98, 13, see="ab-bl-av")
print("ABOVE AVERAGE = {0}\nBELOW AVERAGE = {1}".format(x, y))

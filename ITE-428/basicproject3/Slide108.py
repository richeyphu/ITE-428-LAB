# Slide p.108
def line():
    print("*" * 45)


def avg(s, n):
    return s / n


def get_max(a, b):
    if a > b:
        return a
    return b


def get_min(a, b):
    if a < b:
        return a
    return b


num = int(input("How many student in your class : "))
line()
sum = 0

for i in range(1, num + 1):
    score = float(input("Enter score of student number {} : ".format(i)))
    sum += score
    if i == 1:
        max = min = score
    else:
        max = get_max(max, score)
        min = get_min(min, score)

line()
print("AVERAGE SCORE = {:.2f}".format(avg(sum, num)))
print("MAX SCORE = {:.2f}".format(max))
print("MIN SCORE = {:.2f}".format(min))
line()

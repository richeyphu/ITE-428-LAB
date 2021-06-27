# สร้าง list

def detail(data):  # data รับมาเป็น list
    for i in data:
        print("{}".format(i))


score = []
print("{}".format(score))
print("{}".format(type(score)))
for i in range(5):
    x = int(input('Enter Score : '))
    score.append(x)
print("{}".format(score))
detail(score)


# List Comprehension
# พ.ศ.-543 --> ค.ศ.
c = [(i - 543) for i in range(2500, 2565)]
print("{}".format(c))

dollar = [(i / 31.8) for i in range(1, 101)]
print("{}".format(dollar))

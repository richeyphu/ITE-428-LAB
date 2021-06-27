data1 = 12, 34, 1, 7, 16, 16
data2 = (23, 56, 12, 34, 89, 90, 5.6, 'Adisak')
# print("{}".format(data2))
# print("{}".format(type(data2)))
print("{}".format(data1))
print("{}".format(data1[4]))
print("มีสมาชิก {}".format(len(data1)))
print("มีสมาชิก {}".format(data1.__len__()))  # Dunder Method or Magic Method
print("-" * 10)
for i in range(len(data1)):
    print("{}".format(data1[i]))
print("-" * 10)
for i in data1:  # for -each
    print("{}".format(i))
print("-" * 10)

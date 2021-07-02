student = {"Name": "Adisak",
           "Surname": "Suasaming",
           "Age": 45}

for k, v in student.items():
    print("key = {} , value = {}".format(k, v))
print("-" * 40)

for k in student.keys():
    print("{}".format(k))
print("-" * 40)

for v in student.values():
    print("{}".format(v))

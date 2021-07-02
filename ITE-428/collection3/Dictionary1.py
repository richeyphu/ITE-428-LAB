# Dictionary (json format)
# item --> key , values

student = {"Name": "Adisak",
           "Surname": "Suasaming",
           "Age": 45}
print("{} -- {}".format(student, type(student)))
print("NAME = {}".format(student["Name"]))
student["Name"] = "Archirawit"
print("NAME = {} ".format(student["Name"]))
print("NAME = {} ".format(student))
student["NAME"] = "Archirawit"
print("NAME = {} ".format(student))
del student["NAME"]
print("NAME = {} ".format(student))

from MyLibrary import create_email

Name = input("กรุณากรอกชื่อ : ")
Lastname = input("กรุณากรอกนามสกุล : ")

print("\nอีเมลของคุณคือ {}".format(create_email(Name, Lastname)))

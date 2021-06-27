print("BMI Calculator\n")

weight = float(input("Input your weight (kg.) : "))
height = float(input("Input your height (cm.) : ")) / 100

bmi = weight / height ** 2

print("\nYour BMI = {:15,.2f}".format(bmi))

# print("\nYour BMI = {0:.2f}".format(float(input("Input your weight (kg.) : ")) / ((float(input("Input your height (cm.) : ")) / 100) ** 2)))

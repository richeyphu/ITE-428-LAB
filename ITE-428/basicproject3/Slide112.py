# Slide p.112
def line():
    print("=" * 31)


line()
print("\t\t j        N")
print("\t\t Σ  (i-10)  x i")
print("\t\ti=?")
line()

i = int(float(input("i = ")))
j = int(float(input("j = ")))
N = int(float(input("N = ")))

sum = 0
for i in range(i, j + 1):
    sum += ((i - 10) ** N) * i

line()
print("Sum = {:,}".format(sum))
line()

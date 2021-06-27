# Slide 165

Listdata = []
for i in range(3):
    x = input("Point {} (x,y) : ".format(i + 1))
    y = x.split(' ')
    y = [(int(i)) for i in y]
    Listdata.append(tuple(y))

# a = float(input("Point 1 (x,y) : "))
# b = float(input("Point 2 (x,y) : "))
# c = float(input("Point 3 (x,y) : "))
# A = a.split(' ')
# B = b.split(' ')
# C = c.split(' ')
# x = [tuple(A), tuple(B), tuple(C)]

print("\n{}".format(Listdata))

x1 = Listdata[0][0]
x2 = Listdata[1][0]
x3 = Listdata[2][0]
y1 = Listdata[0][1]
y2 = Listdata[1][1]
y3 = Listdata[2][1]

area = 1 / 2 * abs(x1 * (y2 - y3) - x2 * (y1 - y3) + x3 * (y1 - y2))

print("\nAREA = {:.2f}".format(area))

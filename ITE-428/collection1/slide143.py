import math

x1 = float(input('X1 : '))
y1 = float(input('Y1 : '))
x2 = float(input('X2 : '))
y2 = float(input('Y2 : '))
point1 = x1, y1
point2 = (x2, y2)
# print("{}".format(point1[0]))
x = math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2))

print("\nDistance between two points = {0}".format(x))

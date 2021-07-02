# tuple ()
# list []
# set {}

scoreA = {10, 20, 30, 40, 50, 20, 30}
scoreB = {3, 20, 34, 50, 20, 45, 67, 89, 90}
print("{}".format(scoreA))
print("{}".format(type(scoreA)))
print("Union = {}".format(scoreA | scoreB))
print("Intersection = {}".format(scoreA & scoreB))
print("Difference A-B = {}".format(scoreA - scoreB))
print("Difference B-A = {}".format(scoreB - scoreA))
print("Symmetric Difference = {}".format(scoreA ^ scoreB))  # (A union B) - (A intersect B)

# แก้ไขข้อมูล
score = [10, 56, 67, 88, 98, 3, 21]
print("{}".format(score))
score[0] = 20
print("{}".format(score))
score.append(56)
print("{}".format(score))
score = score + [77, 88, 99]
print("{}".format(score))
del score[3]
print("{}".format(score))
score.sort()
print("{}".format(score))
score.sort(reverse=True)
print("{}".format(score))
print("-" * 30)

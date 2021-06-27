score = [10, 56, 67, 88, 98, 3, 21]
print("{}".format(score))
print("{}".format(type(score)))
print("{}".format(len(score)))
print("{}".format(score.__len__()))
print("-" * 30)
for i in range(len(score)):
    print("{}".format(score[i]))
print("-" * 30)
for i in score:
    print("{}".format(i))
print("-" * 30)
for i, v in enumerate(score):
    print("{}.) {}".format(i + 1, v))

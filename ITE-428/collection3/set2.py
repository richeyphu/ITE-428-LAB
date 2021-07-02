# set / list / tuple

scoreA = [10, 20, 30, 40, 50, 20, 30]
print("{}".format(scoreA))
scoreA = set(scoreA)
print("{}".format(scoreA))
scoreA = list(scoreA)
print("{}".format(scoreA))
scoreA.append(67)
print("{}".format(scoreA))
scoreA = sorted(scoreA)
print("{}".format(scoreA))
scoreA = set(scoreA)
print("{}".format(scoreA))
if 40 in scoreA:
    print("มี")
else:
    print("ไม่มี")

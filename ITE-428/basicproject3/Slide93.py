# Slide p.93
def cal_grade(s):
    if s >= 97:
        return "A+"
    if s >= 93:
        return "A"
    if s >= 90:
        return "A-"
    if s >= 87:
        return "B+"
    if s >= 83:
        return "B"
    if s >= 80:
        return "B-"
    if s >= 77:
        return "C+"
    if s >= 73:
        return "C"
    if s >= 70:
        return "C-"
    if s >= 67:
        return "B-"
    if s >= 63:
        return "C+"
    if s >= 60:
        return "C"
    return "F"


def line():
    print("=" * 40)


def is_bad_score(s):
    if s < 0 or s > 100:
        return True
    return False


def req_valid_score():
    return float(input("Please input the correct score : "))


def cal_score():
    return mid * 0.3 + final * 0.5 + homework * 0.2


line()
print("{:>28}".format("Grade Calculator"))
line()

mid = float(input("Midterm  (100)\t: "))
while is_bad_score(mid):
    mid = req_valid_score()

final = float(input("Final    (100)\t: "))
while is_bad_score(final):
    final = req_valid_score()

homework = float(input("Homework (100)\t: "))
while is_bad_score(homework):
    homework = req_valid_score()

score = cal_score()

line()
# if bad_score(mid) or bad_score(final) or bad_score(homework):
#     print("ERROR: Bad Score")
# else:
print("You got Grade\t{} ({:.2f})".format(cal_grade(score), score))
line()

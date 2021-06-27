def teststr():
    Name = "Adisak"
    print("{}".format(Name))
    print("{}".format(type(Name)))
    print("{}".format(Name.isnumeric()))
    print()


def testfor():
    # for(i = 1; i < 10; i++)
    # range(start,stop,step)
    for i in range(5):
        print("{}".format(i))
    print()
    for i in range(1, 5, 2):
        print("{}".format(i))
    print()

    # for each (traverse)
    score = [12, 34, 56, 12, 78, 17, "seven"]  # List
    for i in score:
        print("{}".format(i))


def testwhile():
    # while() {}, do {} while ();
    i = 1
    while i<=12:
        print("2 X {} = {}".format(i, 2 * i))
        i += 1  # i = i + 1
    i = 1
    while True:
        print("3 X {} = {}".format(i, 3 * i))
        i += 1
        if i == 12:
            break


testwhile()

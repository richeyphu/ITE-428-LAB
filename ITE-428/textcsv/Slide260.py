def readFile(fn):
    with open(file=fn, mode='r', encoding='utf8') as fn:
        data = fn.readlines()
        for i, v in enumerate(data):
            print("{}. {}".format(i + 1, v), end="")


if __name__ == '__main__':
    filename = "myFile/ilovesea.txt"
    readFile(filename)

def readFile(FN):
    with open(file=FN, mode='r', encoding='utf8') as fn:
        for i in fn:
            print("{}".format(i), end="")  # end --> \n


def readFile2(FN):
    with open(file=FN, mode='r', encoding='utf8') as fn:
        data = fn.readlines()  # return all lines as list
        print("{}".format(data))
        print("{}".format(type(data)))
        print("{}".format(data[0]))
        print("Original [{}]".format(data[0]))
        print("Stript   [{}]".format(data[0].strip('\n')))


if __name__ == '__main__':
    filename = "myfile/products.csv"
    # readFile(filename)
    readFile2(filename)

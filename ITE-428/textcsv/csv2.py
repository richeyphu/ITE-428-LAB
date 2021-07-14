import csv


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


def writecsv(data, fn):
    with open(file=fn, mode='a', encoding='utf-8', newline="") as f:
        fw = csv.writer(f, delimiter=",")
        fw.writerows(data)


def readcsv(fn):
    with open(file=fn,mode='r',encoding='utf-8', newline="") as fr:
        fr = csv.reader(fr)
        for i in fr:
            print("Product : {}".format(i))


if __name__ == '__main__':
    filename = "myFile/products.csv"
    # readFile(filename)
    # readFile2(filename)
    readcsv(filename)

    # Ref Slide 276, 280
    # No = int(input("Enter Number of New Product : "))
    # products = []
    # for i in range(No):
    #     product = []
    #     print("\nProduct Number [{}]".format(i + 1))
    #     print("=" * 20)
    #     product.append(input("Enter product Name : "))
    #     product.append(input("Enter product Price : "))
    #     product.append(input("Enter product Stock : "))
    #     products.append(product)
    # print("{}".format(products))
    # writecsv(products, filename)

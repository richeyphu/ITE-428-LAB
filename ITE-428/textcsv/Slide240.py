def writeFile(fn, t):
    with open(file=fn, mode='a', encoding='utf8') as fn:
        for i in t:
            fn.write("{},{},{}\n".format(i[0], i[1], i[2]))


def line():
    print("=" * 20)


if __name__ == '__main__':
    num = int(input("Enter Number of New Product : "))
    textlist = []
    for i in range(1, num + 1):
        print("\nProduct Number [{}]".format(i))
        line()
        name = input("Enter product name   : ")
        price = input("Enter product price  : ")
        stock = input("Enter product stock  : ")
        textlist.append([name, price, stock])
    writeFile("myFile/products.csv", textlist)

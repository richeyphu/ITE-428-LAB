def writeFile(FN):
    fn = open(file=FN, mode='a', encoding='utf8')
    Name = "Adisak Suasaming"
    fn.write("{}\n".format(Name))
    fn.close()


def writefile2(FN):
    with open(file=FN, mode='a', encoding='utf8') as fn:
        Name = "Adisak Suasaming"
        fn.write("{}\n".format(Name))


if __name__ == '__main__':
    filename = 'myFile/mydata.txt'
    # writeFile(filename)
    writefile2(filename)

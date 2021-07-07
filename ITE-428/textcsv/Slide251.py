def readFile(fn):
    with open(file=fn, mode='r', encoding='utf8') as fn:
        data = fn.readlines()
        for i, v in enumerate(sorted(data, reverse=True)):
            print("{}.) {}".format(i + 1, v.upper()), end="")


if __name__ == '__main__':
    filename = "myFile/MarvelComics.txt"
    readFile(filename)

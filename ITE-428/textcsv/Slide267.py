def readFile(fn):
    with open(file=fn, mode='r', encoding='utf8') as fn:
        data = fn.readlines()
        words = []
        for i in data:
            words.append(i.strip('\n'))
    return words


def load_config():
    cfg = "myFile/appConfig.ini"
    return [v.split('=', 1)[1] for v in readFile(cfg)]


if __name__ == '__main__':
    decimal_places, comma, line, currency_unit = load_config()
    comma = "," if comma == "yes" else ""
    total = 0
    for i in readFile("myFile/products267.csv"):
        data = i.split(',')
        price = float(data[1]) * int(data[2])
        total += price
        print("{:<10}{:>19{comma}.{prec}f}".format(data[0],
                                                   price,
                                                   comma=comma,
                                                   prec=decimal_places))
    print(line * 35)
    print("Total Value {:>17{comma}.{prec}f} {unit}".format(total,
                                                            comma=comma,
                                                            prec=decimal_places,
                                                            unit=currency_unit))

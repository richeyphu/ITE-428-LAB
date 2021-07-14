import csv


def readcsv(fn):
    with open(file=fn, mode='r', encoding='utf-8', newline="") as f:
        fr = csv.reader(f)
        next(fr)

        incidents = []
        morefire = []
        alwaysd = []
        lessinj = []
        for i in fr:
            # print("{}".format(i))
            month = i[1]
            f55, f56, f57 = int(i[2]), int(i[3]), int(i[4])
            d55, d56, d57 = int(i[5]), int(i[6]), int(i[7])
            i55, i56, i57 = int(i[8]), int(i[9]), int(i[10])
            mean = (f55 + f56 + f57) / 3
            incidents.append([month, mean])
            if f55 < f56 < f57:
                morefire.append(month)
            if d55 > 0 and d56 > 0 and d57 > 0:
                alwaysd.append(month)
            if i55 > i56 > i57:
                lessinj.append(month)

        for i, v in enumerate(sorted(incidents, reverse=True, key=lambda x: x[1])):
            print("{}.) {} จำนวน {:.2f} ครั้ง".format(i + 1, v[0], v[1]))
        line()

        print("เดือนที่ต้องระวังเนื่องจากมีเหตุการณ์ไฟไหม้มากขึ้นทุกปีที่ผ่านมา คือ", end="")
        for i, v in enumerate(morefire):
            print(" {}".format(v), end=(" ," if i < len(morefire) - 1 else "\n"))
        line()

        print("เดือนที่มีคนตายทุกปี คือ", end="")
        for i, v in enumerate(alwaysd):
            print(" {}".format(v), end=(" ," if i < len(alwaysd) - 1 else "\n"))
        line()

        print("เดือนที่มีคนเจ็บลดลงทุกปี คือ", end="")
        for i, v in enumerate(lessinj):
            print(" {}".format(v), end=(" ," if i < len(lessinj) - 1 else "\n"))
        line()


def line():
    print("-" * 85)


if __name__ == '__main__':
    filename = "myFile/fire.csv"

    line()
    print("\tค่าเฉลี่ย การเกิดเหตุการณ์เพลิงไหม้ ปี 2555-2557")
    line()

    readcsv(filename)

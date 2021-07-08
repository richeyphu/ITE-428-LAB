def readFile(fn):
    with open(file=fn, mode='r', encoding='utf8') as fn:
        data = fn.readlines()
        words = []
        for i in data:
            words.append(i.strip('\n'))
    return words


def writeFile(fn, l):
    with open(file=fn, mode='w', encoding='utf8') as fn:
        fn.writelines(l)


# def is_rude_word(w, r):
#     for i in w:
#         if i in r:
#             return True
#     return False


if __name__ == '__main__':

    rude_word = [word.lower() for word in readFile("myFile/rude_word.txt")]
    comments = [word.lower() for word in readFile("myFile/practice-comment.txt")]

    canshow = []
    cannotshow = []
    num_bad = 0

    for i in comments:
        # if is_rude_word(i.split(' '), rude_word):
        #     cannotshow.append(i + "\n")
        #     num_bad += 1
        # else:
        #     canshow.append(i + "\n")
        if set(i.split(' ')) & set(rude_word):
            cannotshow.append(i + "\n")
            num_bad += 1
        else:
            canshow.append(i + "\n")

    writeFile("myFile/canshow.txt", canshow)
    writeFile("myFile/cannotshow.txt", cannotshow)

    print("Bad Feedback = {:.2f}%".format(num_bad / len(comments) * 100))

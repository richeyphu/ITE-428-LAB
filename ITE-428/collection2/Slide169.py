# Slide 169

def check(w):
    for i in w:
        if i.lower() in rude_word:
            return True
    return False


def is_str_empty(w):
    return not bool(w)


rude_word = ["damn", "hell", "ass", "piss", "silly", "idiotic"]

while True:
    comment = input("Please comment our service : ")
    if is_str_empty(comment):
        break
    elif check(comment.split(" ")):
        print("Cannot show [{}]".format(comment))
    else:
        print("Can show [{}]".format(comment))
    print()

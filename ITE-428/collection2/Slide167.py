# Slide 167

def search(s):
    return s.lower() in [x.lower() for x in flowers]


def is_str_empty(w):
    return not bool(w)


flowers = ["Sun flower", "Ivy", "Jasmine", "Lily"]

while True:
    word = input("Enter flower that you want to search : ")
    if is_str_empty(word):
        break
    print("{}".format(search(word)))

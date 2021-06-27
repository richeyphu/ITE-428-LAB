# Slide 161

def line():
    print("-" * 30)


flowers = ["Sun flower", "Ivy", "Jasmine", "Lily"]

for i, v in enumerate(sorted(flowers)):
    print("{}. {}".format(i + 1, v))
line()

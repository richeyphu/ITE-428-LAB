# Slide182
# Create function Types_of_integer to display result

def checkPrimeNumber(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False


def Types_of_integer(*number):
    x = sorted(set(number))
    for i in x:
        if checkPrimeNumber(i):
            print("{:>5} : Prime Number".format(i))
        else:
            print("{:>5} : Composite Number".format(i))


Types_of_integer(10, 9, 22, 32, 45, 9, 2, 103, 71, 45)
print("-" * 30)
Types_of_integer(49, 37, 14, 37)

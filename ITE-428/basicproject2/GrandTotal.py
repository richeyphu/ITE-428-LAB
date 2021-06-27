# Grand Total Calculation

from MyLibrary import line1, line2, line3
# from MyLibrary import *
# import MyLibrary
# import MyLibrary as ml

price = float(input("Enter Price of Product  : "))
amount = int(input("Enter Amount of Product : "))
subtotal = price * amount

# print("-" * 35)
# call function
line2('#')
# MyLibrary.line2('#')
# ml.line2('#')

print("{0:<14}:{1:>13,.2f} Baht".format("PRICE", price))
print("{0:<14}:{1:>13,}".format("AMOUNT", amount))
print("{0:<14}:{1:>13,.2f} Baht".format("SUBTOTAL", subtotal))

line3('$', 50)
# MyLibrary.line1()
# ml.line3('$', 50)

print("{0:<14}:{1:>13,.2f} Baht".format("VAT (7%)", subtotal * .07))
print("{0:<14}:{1:>13,.2f} Baht".format("GRAND TOTAL", subtotal * 1.07))

line1()
# MyLibrary.line1()
# ml.line1()

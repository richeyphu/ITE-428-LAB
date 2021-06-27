price = float(input("Enter Price of Product\t: "))
amount = int(input("Enter Amount of Product\t: "))

subtotal = price * amount
vat = subtotal * 0.07

print("-" * 35)

print("PRICE\t\t  :{:13,.2f} Baht".format(price))
print("AMOUNT\t\t  :{:13}".format(amount))
print("SUBTOTAL\t  :{:13,.2f} Baht".format(subtotal))

print("-" * 35)

print("VAT (7%)\t  :{:13,.2f} Baht".format(vat))
print("GRAND TOTAL\t  :{:13,.2f} Baht".format(subtotal + vat))

print("-" * 35)

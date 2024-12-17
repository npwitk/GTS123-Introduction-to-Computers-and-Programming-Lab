totalCustomers = int(input("Input (Number of customers): "))
discountCode = input("Input (Discount code): ")
discountPercent = 0

pricePerPerson = 399

if 3 >= totalCustomers >= 1:
    pricePerPerson = pricePerPerson
elif 6 >= totalCustomers >= 4:
    pricePerPerson += 100
else:
    pricePerPerson += 200

subtotalPrice = pricePerPerson * totalCustomers

if discountCode == "CASH":
    discountPercent = 5
elif discountCode == "BIRTHDAY":
    discountPercent = 10
elif discountCode == "COVID":
    discountPercent = 30
else:
    discountPercent = 0

totalPrice = ((100-discountPercent)/100)*subtotalPrice

print("%d person x %.2f baht" % (totalCustomers, pricePerPerson))
print("A subtotal price is %.2f baht" % subtotalPrice)
print("On-top discount %d%%" % discountPercent)
print("A total price is %.2f baht" % totalPrice)


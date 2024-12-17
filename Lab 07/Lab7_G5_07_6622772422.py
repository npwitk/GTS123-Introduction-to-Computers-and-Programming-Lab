notExit = True
sum = 0
item = 0

print("""===================
Cashier Program
===================
""")

while notExit == True:
    eachPrice = float(input("Enter item price or -1 when finished: "))
    if eachPrice != -1:
        sum += eachPrice
        item += 1
    else:
        notExit = False

print()
print("Total purchase amount is %.2f" % sum)
print()

paymentInput = float(input("Your payment: "))
if paymentInput > sum:
    customerChange = paymentInput - sum
    print("You bought %d items today." % item)
    print("Your change is %.2f baht" % customerChange)
else:
    print("You need more money.")
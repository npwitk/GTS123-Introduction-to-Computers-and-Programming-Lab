moneyBalance = int(input("Enter money you have: "))
itemPrice = int(input("Enter price of item: "))

tax = itemPrice * (8/100)
totalPrice = itemPrice + tax

print("Tax: %d" % tax)
print("Total price: %d" % totalPrice)
if moneyBalance >= totalPrice:
    print("yes you have enough money to buy")
else:
    shortfall = totalPrice - moneyBalance
    print("You have shortfall of %d, you cannot buy." % shortfall)
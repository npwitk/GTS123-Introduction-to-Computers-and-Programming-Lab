total = 0
n = 1

print("""Menu:
===============
A - Americano (50)
E - Espresso (40)
G - Green tea (60)""")
print("")

americanoCount = 0
espressoCount = 0
gteaCount = 0

userOrder = input("Input: ")
print("===============")

for x in userOrder:
    if x == "A":
            americanoCount += 1
            print(str(n) + ". Americano 50")
            n += 1
    elif x == "E":
            espressoCount += 1
            print(str(n) + ". Espresso 40")
            n += 1
    elif x == "G":
            gteaCount += 1
            print(str(n) + ". Green tea 60")
            n += 1

allQuantity = americanoCount + espressoCount + gteaCount
total = (50*americanoCount)+(40*espressoCount)+(60*gteaCount)
vat = (0.07*total)
grandTotal = total + vat

print("===============")
print("Quantity: %d" % allQuantity)
print("Vat: %.2f" % vat)
print("Total: %.2f" % total)
print("Grand total: %.2f" % grandTotal)


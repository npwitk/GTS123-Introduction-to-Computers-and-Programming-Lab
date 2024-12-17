from operator import itemgetter

print("Welcome to coin deposit machine")
currentBalance = 0
dictMoney = {}

while True:
    coinInsert = input("Please insert coin: ")
    if coinInsert != "done":
        if int(coinInsert) not in [1,2,5,10]:
            print("Only 1,2,5 and 10 baht coin are allowed")
        else:
            coinInsert = int(coinInsert)

            if coinInsert in dictMoney:
                dictMoney[coinInsert] += 1
            else:
                dictMoney[coinInsert] = 1
            
            currentBalance += coinInsert
            
            print("You inserted %d baht coin" % coinInsert)
            print("Current Balance: %d" % currentBalance)
    else:
        break

print("<-----Deposit Summary----->")

sortedDict = dict(sorted(dictMoney.items(), key=itemgetter(0)))
for key, value in sortedDict.items():
    print("%d baht coins -> %d" % (key,value))
print("Deposit Amount: %d baht" % currentBalance)
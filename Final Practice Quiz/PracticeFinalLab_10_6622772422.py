amountinTHB = 0
answerCollection = []

while True:
    userInput = input("Input: ")
    if userInput == "end":
        break
    else:
        currency, amount = userInput.split()
        amount = float(amount)
        if (currency == "JPY" or currency == "USD" or currency == "EUR") and amount >= 1:
            if currency == "JPY":
                amountinTHB = amount * 0.29
            elif currency == "USD":
                amountinTHB = amount * 31.99
            else:
                amountinTHB = amount * 35.62

            answerCollection.append("%.2f %s is %.2f THB" % (amount, currency, amountinTHB))
            
        else:
            print("ERROR")

for i in range(len(answerCollection)):
    print(answerCollection[i])
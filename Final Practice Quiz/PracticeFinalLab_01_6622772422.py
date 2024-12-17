initialBalance = int(input("Enter the initial balance: "))
currentBalance = initialBalance

while True:
    taInput = input("Transaction type and amount (\"done 0\" to exit): ")
    if taInput == "done 0":
        break
    else:
        transactionType, amount = taInput.split()
        amount = int(amount)
        if transactionType not in ["D","W"] or amount < 0:
            print("Invalid transaction!")
        else:
            if transactionType == "D":
                currentBalance += amount
                print("Deposit = %d THB, current balance = %d THB." % (amount, currentBalance))
            elif transactionType == "W":
                if amount > currentBalance:
                    print("Invalid transaction!")
                    continue
                else:
                    currentBalance -= amount
                    print("Withdrawal = %d THB, current balance = %d THB." % (amount, currentBalance))

print("Current balance = %d THB." % currentBalance)
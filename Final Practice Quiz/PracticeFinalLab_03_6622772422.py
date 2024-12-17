userPoints = 100

while True:
    userInput = input("Command: ")
    if userInput != "done 0":
        type, amount = userInput.split()
        amount = int(amount)
        if type not in ["P","R"] or amount < 0:
            print("Invalid command")
        else:
            if type == "P":
                pointEarned = amount // 50
                userPoints += pointEarned
                print("You earned %d points" % pointEarned)
                print("Your accumulated points = %d points" % userPoints)
            elif type == "R":
                if amount > userPoints:
                    print("Not enough points")
                else:
                    pointDeducted = amount
                    userPoints -= pointDeducted
                    print("You redeemed %d points" % pointDeducted)
                    print("Your accumulated points = %d points" % userPoints)
    else:
        break


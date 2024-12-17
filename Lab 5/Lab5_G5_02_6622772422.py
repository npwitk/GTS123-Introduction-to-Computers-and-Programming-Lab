summation = 0

for x in range(1,6):
    userInput = int(input("Enter an interger #" + str(x) + ": ") )
    summation += userInput

print("The summation is %d." % summation)
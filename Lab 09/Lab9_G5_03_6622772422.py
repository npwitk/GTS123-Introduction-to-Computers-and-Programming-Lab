def UserInput():
    xList = []
    while True:
        numInput = input("Enter an input: ")
        if numInput.isnumeric():
            xList.append(int(numInput))
        elif numInput == "Done":
            break
        else:
            print("Error")
            exit()
    
    return xList

def SumOut(xList):
    sumList = sum(xList)
    print("The summation is %d" % sumList)

def MinOut(xList):
    minList = min(xList)
    print("The minimum is %d" % minList)

def MaxOut(xList):
    maxList = max(xList)
    print("The maximum is %d" % maxList)

xList = UserInput()
print()
SumOut(xList)
MinOut(xList)
MaxOut(xList)


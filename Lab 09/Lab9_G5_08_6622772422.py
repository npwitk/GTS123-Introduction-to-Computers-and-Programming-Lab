lowerBound = int(input("Enter the first number: "))
upperBound = int(input("Enter the upper bound: "))
inputStep = int(input("Enter the step: "))

def myRange(FirstVal, UpperBound, StepSize):
    xList = []
    xList.append(FirstVal)
    addingValue = FirstVal
    while addingValue < UpperBound - StepSize:
        addingValue += StepSize
        xList.append(addingValue)
    print("Range =", xList)

myRange(lowerBound, upperBound, inputStep)
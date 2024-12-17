evenCount = 0
oddCount = 0
notExit = True

while notExit == True:
    integerEach = int(input("Enter an integer (0 to exit): "))
    if integerEach != 0:
        if integerEach % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    else:
        notExit = False

print("----------------------------------")
print("The number of even integers is %d" % evenCount)
print("The number of odd integers is %d" % oddCount)
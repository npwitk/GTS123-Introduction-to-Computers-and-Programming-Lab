notExit = True
sum = 0
no = 0

while notExit == True:
    integerEach = int(input("Enter an integer (-1 to exit): "))
    if integerEach != -1:
        sum += integerEach
        no += 1
    else:
        sum = sum - 1
        notExit = False

print("The sum of %d number(s) is %d."  % (no, sum))
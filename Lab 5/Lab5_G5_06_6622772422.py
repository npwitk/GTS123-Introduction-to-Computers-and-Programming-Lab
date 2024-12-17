for x in range(5):
    inputNumber = int(input("Enter a Number Between 1 and 20: "))
    if inputNumber >= 1 and inputNumber <= 20:
        if inputNumber % 2 == 0:
            print(str(inputNumber) + " is an even number")
        else:
            print(str(inputNumber) + " is an odd number")
    else:
        print("Number is Invalid")
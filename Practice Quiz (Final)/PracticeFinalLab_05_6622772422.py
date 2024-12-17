while True:
    numInput = int(input("Enter an integer number (0 to exit): "))
    space = numInput - 1
    if numInput != 0:
        if 1 <= numInput <= 9:
            for i in range(1, numInput+1):
                string = str(numInput) + " "
                print((" " * space) + (string * i))
                space -= 1
        else:
            print("Valid value is between 0 and 9!")
            break
    else:
        print("Exit program. Bye!")
        break
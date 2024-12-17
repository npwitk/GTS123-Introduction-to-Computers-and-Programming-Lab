A,B,C = input("Please enter an input: ").split("*")


if A.isnumeric() and B.isnumeric() and C.isnumeric():
    if int(A) >= 1 and int(B) >= 1 and int(C) >= 1:
        choiceOption = input("Please enter your choice (1 or 2): ")
        choiceOption = int(choiceOption)
        if choiceOption == 1 or choiceOption == 2:
            if choiceOption == 1:

                A = int(A)
                B = int(B)
                C = int(C)

                outputOption1 = A + ((B**2)+(C**3))**(1/2)
                print("The output is %.2f" % outputOption1)
            else:
                
                A = str(A)
                B = str(B)
                C = int(C)

                numerator = A + B

                numerator = int(numerator)
                
                outputOption2 = numerator % C
                print("The output is %.2f" % outputOption2)
        else:
            print("Invalid Inputs")
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")
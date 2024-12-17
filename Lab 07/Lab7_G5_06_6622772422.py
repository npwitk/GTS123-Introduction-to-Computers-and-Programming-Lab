notExit = True

while notExit == True:
    print("""
===== MAIN MENU =====
1. Addition
2. Subtraction
3. Exit
          """)
    choiceSelect = int(input("Select an operation (1-3): "))
    if choiceSelect == 1 or choiceSelect == 2:
        firstNo, secondNo = input("Enter two numbers: ").split()
        firstNo = int(firstNo)
        secondNo = int(secondNo)
        if choiceSelect == 1:
            ans = firstNo + secondNo
            print("%d + %d = %d" % ((firstNo),(secondNo),(ans)))
        else:
            ans = firstNo - secondNo
            print("%d - %d = %d" %((firstNo),(secondNo),(ans)))
    elif choiceSelect == 3:
        print("Bye!!!")
        notExit = False
    
    
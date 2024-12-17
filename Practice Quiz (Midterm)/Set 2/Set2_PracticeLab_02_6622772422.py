x1, x2 = input("Please enter your information: ").split(",")

def printOut():
    print("Your name is %s." % userName)
    print("Your age is %d." % userAge)

if x1.isnumeric() and x2.isalpha() and 120 >= int(x1) >= 0:
    userAge = x1
    userAge = int(userAge)
    userName = x2
    printOut()
elif x1.isalpha() and x2.isnumeric() and 120 >= int(x2) >= 0:
    userAge = x2
    userAge = int(userAge)
    userName = x1
    printOut()
else:
    print("Please enter your complete information.")
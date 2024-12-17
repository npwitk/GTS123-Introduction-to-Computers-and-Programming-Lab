print("========== Welcome to Hi! Car Wash ==========")
totalPrice = 0
washType = input("Choose your serivces: W=Wash C=Wash+Vacuum ")
if washType == 'W':
    totalPrice = 100
elif washType == 'C':
    totalPrice = 120
else:
    print("Please Choose Your Services")
if washType == 'W' or washType == 'C':
    carSize = input("Enter your car size: \"S\", \"M\", \"L\": ")
    if carSize == 'S':
        totalPrice = totalPrice
    elif carSize == 'M':
        totalPrice = totalPrice + 20
    elif carSize == 'L':
        totalPrice = totalPrice + 40
    else:
        print("You Enter the wrong car size")
    
    if carSize == 'S' or carSize == 'M' or carSize == 'L':
        print("Price =", totalPrice,"Baht")
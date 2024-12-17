firstNo, secondNo = input("Please enter two integers: ").split() ## Default of .split is already a space

if firstNo.isnumeric() and secondNo.isnumeric():

    firstNo = int(firstNo)
    secondNo = int(secondNo)

    if 30 >= firstNo >= 1 and 30 >= secondNo >= 1:
        if firstNo > secondNo:
            maxNo = firstNo
            minNo = secondNo
        else:
            maxNo = secondNo
            minNo = firstNo
        ## หรือจะใช้ max(array) ก็ได้

        print("The minimum number is %d" % minNo)
        print("The maximum number is %d" % maxNo)

        insideSummation = 0 
        for x in range(minNo, maxNo+1):
            insideSummation += x

        answer = (insideSummation)**(1/2)

        print("The square root of the summation is %.2f" % answer)

    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")
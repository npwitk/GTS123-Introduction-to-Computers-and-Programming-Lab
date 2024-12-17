inputSpeed = int(input("Enter speed in mph: "))

if inputSpeed >= 1:
    inputDistance = input("Enter distance in miles: ")

    if inputDistance.isnumeric():
        inputDistance = int(inputDistance)
        if inputDistance >= 1:
            outputFormat = input("Enter output format (D or M): ")
            if outputFormat == "D" or outputFormat == "M":

                ## Calculation

                timeOutput = inputDistance/inputSpeed

                print("At %d mph, it will take" % inputSpeed)
                if outputFormat == "D":
                    print("%d hours to travel %d miles." % (timeOutput, inputDistance))
                else:
                    ## Calculation

                    hourOutputRounded = inputDistance//inputSpeed
                    minuteOutput = ((inputDistance/inputSpeed)-hourOutputRounded)*60

                    print("%d hours and %d minutes to travel %d miles." % (hourOutputRounded, minuteOutput, inputDistance))
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
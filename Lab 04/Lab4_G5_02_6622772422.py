print("Fever Symptoms Advisor Program")
inputTemp = float(input("Check your body temperature in F = "))
if inputTemp >= 100.4:
    print("You got a fever.")
    inputTreatment = input("Choose your treatment: 1 = medication 2 = no medication ")
    if inputTreatment == '1':
        print("Take Tylenol every 4 hours as needed")
    elif inputTreatment == '2':
        print("Taking a bath in lukewarm water or get the cool packs")
    else:
        print("You choose the wrong choice")
else:
    print("You are fine.")
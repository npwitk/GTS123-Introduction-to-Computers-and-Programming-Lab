def UserInput():
    weight = float(input("Input your weight (kilogram): "))
    height = float(input("Input your height (metre): "))

    return weight, height

def FindBMI(ww, hh):
    UserBMI = ww/(hh**2)

    return UserBMI

def ShowBMI(MyBMI):
    print("The user BMI is %.2f" % MyBMI)

ww, hh = UserInput()
UserBMI = FindBMI(ww, hh)
ShowBMI(UserBMI)
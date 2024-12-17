gradeITS100 = float(input("enter grade from ITS100: "))
gradeEL171 = float(input("enter grade from EL171: "))
gradeSCS183 = float(input("enter grade from SCS183: "))

GPA = ((3*gradeITS100)+(3*gradeEL171)+(1*gradeSCS183))/(3+3+1)

print("Your GPA is %.2f" % GPA)
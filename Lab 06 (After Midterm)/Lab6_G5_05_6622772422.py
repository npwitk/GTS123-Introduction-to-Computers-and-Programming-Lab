loopTime = int(input("how many persons in a group? : "))
groupName = "ABC"
listGrade = []

for x in groupName:
    print("please enter grade from group", x)
    for y in range(loopTime):
        inputGrade = float(input("enter grade: "))
        listGrade.append(inputGrade)
    if x == "A":
        gradeA = listGrade
        listGrade = []
    elif x == "B":
        gradeB = listGrade
        listGrade = []
    elif x == "C":
        gradeC = listGrade
        listGrade = []

print("the highest grade of group A is %.1f" % (max(gradeA)))
print("the highest grade of group B is %.1f" % (max(gradeB)))
print("the highest grade of group C is %.1f" % (max(gradeC)))


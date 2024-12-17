firstNo=input("Enter the 1st number: ")
secondNo=input("Enter the 2nd number: ")
thirdNo=input("Enter the 3rd number: ")

firstNo=float(firstNo)
secondNo=float(secondNo)
thirdNo=float(thirdNo)

print("a,b,c = %.2f, %.2f, %.2f" %(firstNo,secondNo,thirdNo))

average=(firstNo+secondNo+thirdNo)/3
sum=(firstNo+secondNo+thirdNo)
multiplication=(firstNo*secondNo*thirdNo)

print("The average of three integers = %.2f" %average)
print("The summation of three integers = %.2f" %sum)
print("The multiplication of three integers = %.2f" %multiplication)

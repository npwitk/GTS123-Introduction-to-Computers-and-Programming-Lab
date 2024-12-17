intNo = int(input("Enter an integer nimber (n>0): "))

print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")
operationSelect = int(input("Select operation: "))

if operationSelect == 1:
    factOfN = 1
    for x in range(1,intNo+1):
        factOfN = factOfN * x
    print("Factorial of n (n!) =", factOfN)
elif operationSelect ==2:
    summation = 0
    for x in range(1,intNo+1):
        summation = summation + x
    print("Summation of n integers =", summation)
else:
    print("N/A Operation!")
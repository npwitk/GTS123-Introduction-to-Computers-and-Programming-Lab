inputA = int(input("Input: a=? "))
inputB = int(input("Input: b=? "))
inputC = int(input("Input: c=? "))

if inputA >= 1 and inputB >= 1 and inputC >= 1:
    triangle = [int(inputA), int(inputB), int(inputC)]
    big = max(triangle) ## THIS IS NEW
    triangle.remove(big)
    if big < sum(triangle):
        print("Output: Form a triangle")
    else:
        print("Output: Can't form a triangle")
else:
    print("Some input is not a number.")
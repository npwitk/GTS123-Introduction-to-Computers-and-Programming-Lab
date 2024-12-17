print("========================")
ans = 0
list1 = []
for x in range(1,6):
    n = int(input("Input#%d: "%x))
    list1.append(n)

selectOption = input("Select the option: 1) Summation, 2) Average, 3) Min, 4) Max ...: ")
selectOption = int(selectOption)
if selectOption == 1:
    ans = sum(list1)
elif selectOption == 2:
    ans = sum(list1)/5
elif selectOption == 3:
    ans = min(list1)
elif selectOption == 4:
    ans = max(list1)

print("Your result is %d" % ans)

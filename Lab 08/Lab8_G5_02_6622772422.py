num = []
a = {}
x = 1
num = input("Input: ").split()
for i in num:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
for i in a.keys():
    if i.isnumeric() and int(i) != a[i]:
        x = 0
if x == 1:
    print("Output: good sequence")
else:
    print("Output: not good sequence")
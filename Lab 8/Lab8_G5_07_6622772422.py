a = input("input sequence1: ").split()
b = input("input sequence2: ").split()

set1 = []
set2 = []

for i in a:
    if i.isdigit():
        set1.append(i)

for i in b:
    if i.isdigit():
        set2.append(i)

set3 = set(set1)
set4 = set(set2)

if set3 & set4:
    print("output: True")
else:
    print("output: False")
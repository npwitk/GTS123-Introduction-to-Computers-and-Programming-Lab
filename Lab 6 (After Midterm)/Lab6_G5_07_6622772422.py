import random as r

list1 = []
shuffledList = []

for x in range(1,5):
    n = input("Enter string#%d: "%x)
    list1.append(n)

r.shuffle(list1)

print("Random order of sentence: ", end="")
for i in range(4):
    print(list1[i], end=" ")

evenNo = 0
oddNo = 0

for x in range(5):
    userInput = int(input("Enter a Number: "))
    if userInput % 2 == 0:
        evenNo += 1
    else:
        oddNo +=1
print("There were %d even numbers" % evenNo)
print("There were %d odd numbers" % oddNo)
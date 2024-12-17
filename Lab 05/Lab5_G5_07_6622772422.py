validResponse = 1
likeNo = 0
sadNo = 0
heartNo = 0

for x in range(10):
    userInput = input("Feeling Like (\"L\"), Sad (\"S\"), and Heart(\"H\")? ")
    if userInput in "LSH":
        validResponse += 1
        if userInput == "L":
           likeNo += 1
        elif userInput == "S":
           sadNo += 1
        else:
           heartNo += 1
    else:
        print("Invalid input, accepts only (L/S/H).")

print("============")
print("Total is", (validResponse-1))
print("============")

likePercent = (likeNo/(validResponse-1))*100
sadPercent = (sadNo/(validResponse-1))*100
heartPercent = (heartNo/(validResponse-1))*100

print("Like: %d (%.2f%%)" % (likeNo, likePercent))
print("Sad: %d (%.2f%%)" % (sadNo, sadPercent))
print("Heart: %d (%.2f%%)" % (heartNo, heartPercent))



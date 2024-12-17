stu_dict = {}
n = 0

while True:
    userInput = input("Enter student ID and score: ")
    if userInput == "done 0":
        break
    else:
        stuID, score = userInput.split()
        score = int(score)
        if len(stuID) == 4 and stuID.isnumeric():
            if stuID not in stu_dict:
                if 100 >= score >= 0:
                    stu_dict[stuID] = score
                    n += 1
                else:
                    print("Invalid score!")
            else:
                print("The ID is already recorded!")
        else:
            print("Invalid ID format!")

def stuPrint():
    for k, v in stu_dict.items():
        print(k, v)

print("List:")
if stu_dict != {}:
    stuPrint()

    summation = sum(stu_dict.values())
    average = summation / n
    print("There are %d student(s). The average score is %.2f points." % (len(stu_dict), average))
else:
    print("no score is recorded!")
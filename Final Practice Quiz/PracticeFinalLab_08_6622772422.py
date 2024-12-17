from operator import itemgetter

dict_frequency = {}

while True:
    userInput = input("Input: ")
    if userInput != "done":
        if userInput.isnumeric() and 0 <= int(userInput) <= 1000:
            if int(userInput) in dict_frequency:
                dict_frequency[int(userInput)] += 1
            else:
                dict_frequency[int(userInput)] = 1
        else:
            print("ERROR")
    else:
        break
    
print("----SUMMARY----")

sortedDict = dict(sorted(dict_frequency.items(), key=itemgetter(0)))
if sortedDict == {}:
    print("The list is empty")
else:
    for key, value in sortedDict.items():
        print(key, value)

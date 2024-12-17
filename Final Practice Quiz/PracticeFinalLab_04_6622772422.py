from operator import itemgetter

players = {}

while True:
    userInput = input("Input: ")
    if userInput == "done":
        break
    else:
        name, score = userInput.split()
        if score.isnumeric() and int(score) >= 0:
            score = int(score)
            if name not in players:
                players[name] = score
            else:
                print("Duplicated player")
        else:
            print("Invalid input")

sortedDict = dict(sorted(players.items(), key=itemgetter(1), reverse=True))

if sortedDict == {}:
    print("No players")
else:

    avg = sum(sortedDict.values())/len(sortedDict)
    prizeMedal = ""

    for key, value in sortedDict.items():
        if value == max(sortedDict.values()):
            prizeMedal = "Gold"
        elif value >= avg:
            prizeMedal = "Silver"
        else:
            prizeMedal = ""
        print(str(key) + "\t" + str(value) + "\t" + prizeMedal)
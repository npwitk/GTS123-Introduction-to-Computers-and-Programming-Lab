from operator import itemgetter

info_dict = {}

def dick(n,s):
    info_dict[n] = s
    return info_dict

while True:
    initialInput = input("Enter student name and score: ")
    if initialInput == "end 0":
        break
    else:
        name, score = initialInput.split()
        score = int(score)
        if name not in info_dict:
            if 0 <= score <= 100:
                dick(name,score)
            else:
                print("Invalid score!")
        else:
            print("Duplicate name!")

if info_dict == {}:
    print("empty list!")
else:
    sort_dict = dict(sorted(info_dict.items(), key=itemgetter(1), reverse=True))
    for key, value in sort_dict.items():
        print(key, "\t", value)
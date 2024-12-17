from operator import itemgetter

dictGrade = {}; ceCount = 0; cheCount = 0; ecCount = 0; ieCount = 0; meCount = 0

while True:
    userInput = input("Input: ")
    if userInput == "done":
        break
    else:
        name, pref, grade = userInput.split()
        grade = float(grade)
        if pref not in ["ce","che","ec","ie","me"] or grade > 4.0 or grade < 0.0:
            print("ERROR")
        else:
            if pref == "ce":
                ceCount += 1
            elif pref == "che":
                cheCount += 1
            elif pref == "ec":
                ecCount += 1
            elif pref == "ie":
                ieCount += 1
            elif pref == "me":
                meCount += 1
            
            string = name + " " + pref
            dictGrade[string] = grade


print("----SUMMARY----")
print("ce =", ceCount)
print("che =", cheCount)
print("ec =", ecCount)
print("ie =", ieCount)
print("me =", meCount)

sorted_dict = dict(sorted(dictGrade.items(), key=itemgetter(1), reverse=True))

print("----LIST----")
if dictGrade == {}:
    print("The list is empty.")

for key, value in sorted_dict.items():
    print(key, value)
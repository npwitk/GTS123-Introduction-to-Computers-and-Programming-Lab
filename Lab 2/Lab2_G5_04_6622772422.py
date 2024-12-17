fullScore=input("Input Full Score = ")
realScore=input("Input Real Score = ")

fullScore=float(fullScore)
realScore=float(realScore)

percentage=(realScore/fullScore)*100

print("----------------------------")
print("--- Calculate Percentage ---")
print("----------------------------")

print("Full Score:", fullScore)
print("Real Score:", realScore)

print("----------------------------")
print("Percentage:", percentage, "%")
print("----------------------------")
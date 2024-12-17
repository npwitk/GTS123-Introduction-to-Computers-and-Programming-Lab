inputDays = input("Input number of days: ")
inputDays = int(inputDays)
inputHours = input("Input number of hours: ")
inputHours = int(inputHours)

totalSecond = (inputDays*24)*60*60+(inputHours*60*60)
totalMinute = ((inputDays*24)*60)+(inputHours*60)

inputOptions = input("""Please select a choice:
1-to calculate the total number of seconds or
2-to calculate the total number of minutes
Enter your selected choice: """)

if inputOptions == '1':
    print("------------------------------------------------")
    print("The total number of seconds are", totalSecond)
else:
    print("------------------------------------------------")
    print("The total number of minutes are", totalMinute)
hour,min,second = input("Input: ").split(":")

hour = int(hour)
min = int(min)
second = int(second)

totalFromHour = hour * 3600
totalFromMin = min * 60
totalFromSecond = second

if hour <= 23 and hour >= 0 and min <= 59 and min >= 0 and second <= 59 and second >= 0:
    totalAll = totalFromHour + totalFromMin + totalFromSecond
    print("The number of seconds =", totalAll)
else:
    print("Invalid time")
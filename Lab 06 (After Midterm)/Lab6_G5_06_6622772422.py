rawData = input("Enter  dd/mm/yyyy: ")

if len(rawData) == 8:
    date = rawData[0:2] #This will be string
    month = rawData[2:4]
    yearOG = rawData[4:8]

    date = int(date)
    month = int(month)
    yearOG = int(yearOG)  

    year = yearOG - 543

    if 12 >= month >= 1:
        print("Date = %02d" % date) #if they insist
        print("Month = %d" % month)
        print("Year = %d" % year)
    else:
        print("Error! There're 12 months")
else:
    print("Please enter 8 digits!!")
parkingMinute = int(input("Input parking time (in minutes): "))

parkingFee = ((parkingMinute//60)*20)

excessM = parkingMinute % 60

if excessM > 15:
    parkingFee = parkingFee + 20

print(f"The charge is {parkingFee} baht.")
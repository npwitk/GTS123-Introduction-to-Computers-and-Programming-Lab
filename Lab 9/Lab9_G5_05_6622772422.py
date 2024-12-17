def SeatType():
    seat = ""
    while seat not in ["P","D","H"]:
        seat = input("Select the seat type (P or D or H): ")

        if seat in ["P","D","H"]:
            break
        else:
            print("Wrong seat type! Please select again.")
    
    return seat


def MovieType():
    movie = ""
    while movie not in ["1","2"]:
        movie = input("Select the movie type (1 or 2): ")

        if movie in ["1","2"]:
            break
        else:
            print("Wrong movie type! Please select again.")

    return movie

def TicketPrice(seat, movie):
    if seat == "P" and movie == "1":
        print("The ticket price is 100")
    elif seat == "P" and movie == "2":
        print("The ticket price is 120")
    elif seat == "D" and movie == "1":
        print("The ticket price is 140")
    elif seat == "D" and movie == "2":
        print("The ticket price is 200")
    elif seat == "H" and movie == "1":
        print("The ticket price is 400")
    elif seat == "H" and movie == "2":
        print("The ticket price is 500")

s = SeatType()
m = MovieType()
TicketPrice(s,m)
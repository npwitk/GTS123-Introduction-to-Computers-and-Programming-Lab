nameList = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]

q = False

while q == False:
    print("Student list:", nameList)
    userDel = input("Please enter a student's name that you want to delete (q = exit): ")
    if userDel == "q":
        q = True
    else:
        selectOption = input("""You will remove ' %s ' from this class.
Please type (Confirm 'y', Cancel 'n'): """% userDel)
        if selectOption == "y":
            nameList.remove(userDel)
exit()
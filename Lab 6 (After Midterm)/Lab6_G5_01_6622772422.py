list1 = input("Enter a comma-separated list: ").split(",")

for i in list1:
    for j in list1:
        for k in list1:
            if i != j and i != k and j != k:
                print(i,j,k)
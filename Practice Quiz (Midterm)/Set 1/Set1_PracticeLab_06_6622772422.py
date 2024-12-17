baseWanted = 0

inputDNA = input("DNA: ")
baseOption = input("Base: ")

## Check 2 things: DNA is valid (A,T,C,G) (Harder) and Base is valid (A,T,C,G)
if baseOption in "ATCG":
    for x in inputDNA:
        if x == baseOption:
            print("c:", x)
            print("Counted")
            baseWanted += 1
        else:
            print("c:", x)
    print("There are %d times that the base %s occur in this DNA." % (baseWanted, baseOption))
else:
    print("This is not DNA String")


while True:
    seq1 = input("Input Sequence 1: ").split() ## จะได้ออกมาเป็น list
    seq2 = input("Input Sequence 2: ").split()

    seq1 = [i for i in seq1 if i.isnumeric()] ##กลั่นกรอง
    seq2 = [i for i in seq2 if i.isnumeric()]

    seq1, seq2 = set(seq1), set(seq2)

    if seq1 == seq2:
        print("Output: same set")
    else:
        print("Output: different set")
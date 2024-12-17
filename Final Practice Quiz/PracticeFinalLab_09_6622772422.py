## เหนื่อย ไม่ชอบ ไม่ทำ ลอกปันปัน จบมาก

passed = True
n = 0
xo_list = []
while n < 9:
    ui = input("Input: ")
    if ui in ('x', 'o'):
        n += 1
        xo_list.append(ui)
    else:
        print("Wrong input")
        passed = False
        break

if passed:
    run = 0
    for row in range(7):
        if row % 2 == 0:
            print('-------')
        else:
            print('|', end='')
            for col in range(3):
                print('%s'% xo_list[run], end='|')
                run += 1
            print()
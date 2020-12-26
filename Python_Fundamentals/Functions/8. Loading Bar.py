enter = int(input())

al_bet = str(enter)
simbol = int(al_bet[0])
point = 10 - simbol


def print_rez():
    ls1 = "%" * simbol
    ls2 = "." * point

    if enter == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f'{enter}% [{ls1}{ls2}]')
        print("Still loading...")


print_rez()

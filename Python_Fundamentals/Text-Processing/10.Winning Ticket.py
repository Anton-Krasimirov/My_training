def is_win_simbol(string):
    if one.count("@") >= 12:
        return "@"
    elif one.count("$") >= 12:
        return "$"
    elif one.count("#") >= 12:
        return "#"
    elif one.count("^") >= 12:
        return "^"


data = input().replace(" ", "")
tickets = data.split(",")

for one in tickets:
    if len(one) != 20:
        print("invalid ticket")
        continue
    left = one[:10]
    right = one[10:]
    win_simbol = is_win_simbol(one)

    if win_simbol is None or win_simbol * 6 not in left or win_simbol * 6 not in right:
        print(f'ticket "{one}" - no match')
        continue

    if left.count(win_simbol) == 10 and left == right:
        print(f'ticket "{one}" - 10{win_simbol} Jackpot!')
        continue
    else:
        count = ""
        if left.count(win_simbol) <= right.count(win_simbol):
            count = str(left.count(win_simbol)) + win_simbol
        else:
            count = str(right.count(win_simbol)) + win_simbol
        print(f'ticket "{one}" - {count}')

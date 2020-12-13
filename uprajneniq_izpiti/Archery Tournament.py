targets = list(map(int, input().split('|')))

points = 0

command = input()
while not command == 'Game over':
    data = command.split()
    type = data[0]
    if type == "Shoot":
        direct, start_i, lenght = data[1].split("@")
        start_i = int(start_i)
        lenght = int(lenght)
        if start_i in range(len(targets)):
            if direct == "Left":
                formula = (start_i - lenght) % len(targets)
            else:
                formula = (start_i + lenght) % len(targets)

            if targets[formula] < 5:
                points += targets[formula]
                targets[formula] = 0
            else:
                points += 5
                targets[formula] -= 5

    elif type == "Reverse":
        targets = targets[::-1]
    command = input()

print(" - ".join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")
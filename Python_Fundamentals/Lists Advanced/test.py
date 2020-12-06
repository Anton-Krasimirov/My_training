targets = [int(x) for x in input().split()]

shoot = input()
while not shoot == "End":
    shoot = shoot.split()
    command = shoot[0]
    idx = int(shoot[1])
    power = int(shoot[2])
    if command == "Shoot":
        if idx > len(targets) or idx < 0:
            shoot = input()
            continue
        targets[idx] -= power
        if targets[idx] <= 0:
            targets.remove(targets[idx])
    elif command == "Add":
        if idx > len(targets) or idx < 0:
            print("Invalid placement!")
            shoot = input()
            continue
        targets.insert(idx, power)
    elif command == "Strike":
        start_index = idx - power
        end_index = idx + power
        if not end_index + 1 > len(targets) or not start_index < 0:
            targets = targets[:start_index] + targets[end_index + 1:]
        else:
            print("Strike missed!")
            shoot = input()
            continue

    shoot = input()
print("|".join([str(x) for x in targets]))
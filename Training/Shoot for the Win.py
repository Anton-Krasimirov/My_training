targets = [int(x) for x in input().split()]


count = 0
data = input()
while not data == "End":
    data = int(data)
    if not data < 0 and not data > len(targets) - 1:
        if not targets[data] == -1:
            value = targets[data]
            targets[data] = -1
            count += 1
            for i in range(len(targets)):
                if targets[i] == -1:
                    continue
                elif targets[i] <= value:
                    targets[i] += value
                else:
                    targets[i] -= value

    data = input()

print(f"Shot targets: {count} -> {' '.join([str(x) for x in targets])}")
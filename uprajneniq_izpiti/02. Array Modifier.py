list = list(map(int, input().split()))

command = input()

while command != "end":
    token = command.split()
    command = token[0]
    if len(token) == 3:

        idx1 = int(token[1])
        idx2 = int(token[2])

    if command == "swap":
        list[idx1], list[idx2] = list[idx2], list[idx1]

    elif command == "multiply":
        list[idx1] *= list[idx2]

    elif command == "decrease":
        list = [num - 1 for num in list]

    command = input()
print(list)

in_list = [int(x) for x in input().split()]


count = 0
command = input().split()

while command[0] != "end":
    if command[0] == "swap":
        idx_a = int(command[1])
        idx_b = int(command[2])
        if idx_a < len(in_list) and idx_a >= 0 and idx_b < len(in_list) and idx_b >= 0:
            in_list[idx_a], in_list[idx_b] = in_list[idx_b], in_list[idx_a]
            print(in_list)
        else:
            print(in_list)
        count += 1


    elif command[0] == "enumerate_list":
        print(list((i, n) for i, n in enumerate(in_list)))
        count += 1

    elif command[0] == "max":
        print(max(in_list))
        count += 1

    elif command[0] == "min":
        print(min(in_list))
        count += 1


    elif command[0] == "get_divisible":
        print(list(i for i in in_list if i % int(command[2]) == 0))
        count += 1
    command = input().split()


print(count)














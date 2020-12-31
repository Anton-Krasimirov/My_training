niz = [x for x in input().split()]

data = input()
while not data == "end":
    command = data.split()[0]
    if command == "reverse":
        idx = int(data.split()[2])
        idx2 = int(data.split()[4])
        pies = niz[idx:idx + idx2]
        pies.reverse()
        niz = niz[:idx] + pies + niz[idx + idx2:]
    elif command == "sort":
        idx = int(data.split()[2])
        idx2 = int(data.split()[4])
        pies = niz[idx:idx + idx2]
        pies.sort()
        niz = niz[:idx] + pies + niz[idx + idx2:]
    elif command == "remove":
        x = int(data.split()[1])
        for i in range(x):
            niz.pop(0)

    data = input()




print(", ".join(niz))
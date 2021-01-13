from collections import deque

def decision():
    names = deque()
    while True:
        command = input()
        if command == "End":
            print(f"{len(names)} people remaining.")
        elif command == "Paid":
            while names:
                print(names.popleft())
        else:
            names.append(command)


decision()
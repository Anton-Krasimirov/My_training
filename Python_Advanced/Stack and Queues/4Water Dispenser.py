from collections import deque

all_water = int(input())
names = deque()
while True:
    command = input()
    if command == "Start":
        break
    names.append(command)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{all_water} liters left")
        break
    elif command[0] == "refill":
        all_water += int(command[1])
    else:
        person_watr = int(command[0])
        if person_watr <= all_water:
            person = names.popleft()
            all_water -= person_watr
            print(f'{person} got water')
        else:
            print(f'{person} must wait')



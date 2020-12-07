n = int(input())
parking = {}
for i in range(n):
    line = input().split()
    command = line[0]
    name = line[1]
    if command == "register":
        car = line[2]
        if name not in parking:
            parking[name] = car
            print(f'{name} registered {car} successfully')
        else:
            print(f"ERROR: already registered with plate number {car}")

    else:
        if name in parking:
            parking.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")


for name, car in parking.items():
    print(f'{name} => {car}')


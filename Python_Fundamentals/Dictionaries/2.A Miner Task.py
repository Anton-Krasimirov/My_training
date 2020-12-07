diction = {}

resource = input()
while resource != "stop":
    quantity = int(input())
    if resource not in diction:
        diction[resource] = 0
    diction[resource] += quantity
    resource = input()


for key, value in diction.items():
    print(f"{key} -> {value}")
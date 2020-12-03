train = int(input())

wagons = [0] * train

while True:
    comand = input()
    tokens = comand.split(" ")  # .split vrashta string
    com = tokens[0]
    if comand == "End":
        break

    if com == "add":
        people = int(tokens[1])
        wagons[-1] += people
    elif com == "insert":
        idx = int(tokens[1])# index = na chisloto ot poziciq 1 na token
        people = int(tokens[2])
        wagons[idx] += people
    elif com == "leave":
        idx = int(tokens[1])
        people = int(tokens[2])
        wagons[idx] -= people


print(wagons)

# vagons = int(input())
# train = [0] * vagons
#
#
# while True:
#     command = input()
#     tokens = command.split(" ")# .split vrashta string
#     command = tokens[0]
#     if command == "End":
#         break
#
#     if command == "add":
#         people = int(tokens[1])
#         train[-1] += people
#     elif command == "insert":
#         index = int(tokens[1])# index = na chisloto ot pziciq 1 na token
#         people = int(tokens[2])
#         train[index] += people# index e число в train и прибавяме към него
#     elif command == "leave":
#         index = int(tokens[1])
#         people = int(tokens[2])
#         train[index] -= people# тук имаме изваждане от index
#
# print(train)
















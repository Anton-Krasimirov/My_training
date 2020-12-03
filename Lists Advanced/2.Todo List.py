command = input()

list = [0] * 10

while True:
    if command == "End":
        break
    taken = command.split("-", maxsplit=1)
    importance = int(taken[0])
    value = taken[1]
    list.insert(importance, value)
    command = input()

todo_note = [x for x in list if x != 0]


print(todo_note)



# command = input()
#
# list = []
#
# while True:
#     if command == "End":
#         break
#     taken = command.split("-", maxsplit=1)
#     importance = int(taken[0])
#     value = taken[1]
#     list.append((importance, value))
#     command = input()
#
# todo_note = [value for importance, value in sorted(list)]
#
# print(todo_note)
shopping_list = [x for x in input().split("!")]


data = input()
while data != "Go Shopping!":
    command = data.split()[0]
    item = data.split()[1]
    if command == "Urgent":
        if not item in shopping_list:
            shopping_list.insert(0, item)
    elif command == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif command == "Correct":
        newitem = data.split()[2]
        if item in shopping_list:
            idx = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.insert(idx, newitem)
    elif command == "Rearrange":
        if item in shopping_list:
            idx = shopping_list.index(item)
            artc = shopping_list.pop(idx)
            shopping_list.append(artc)


    data = input()
print(", ".join(shopping_list))
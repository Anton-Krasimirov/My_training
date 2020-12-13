collekting = input().split(", ")
items = []
for i in collekting:
    items.append(i)
command = input()
while command != "Craft!":
    index = command.split(" - ")
    command = index[0]
    item = index[1]
    if command == "Collect":
        if item not in items:
            items.append(item)
    if command == "Drop":
        if item in items:
            items.remove(item)
    if command == "Combine Items":
        combination = item.split(":")
        item1 = combination[0]
        item2 = combination[1]
        if item1 in items:
            idx = items.index(item1)
            items.insert(idx + 1, item2)
    if command == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()
print(", ".join(items))

cards = [x for x in input().split(", ")]

n = int(input())

for i in range(n):
    data = input()
    command = data.split(", ")[0]
    if command == "Add":
        card = data.split(", ")[1]
        if card in cards:
            print("Card is already bought")
        else:
            cards.append(card)
            print("Card successfully bought")

    elif command == "Remove":
        card = data.split(", ")[1]
        if card in cards:
            print("Card successfully sold")
            cards.remove(card)
        else:
            print("Card not found")

    elif command == "Remove At":
        idx = int(data.split(", ")[1])
        if idx in range(len(cards)):
            cards.pop(idx)
            print("Card successfully sold")
        else:
            print("Index out of range")
    elif command == "Insert":
        idx = int(data.split(", ")[1])
        card = data.split(", ")[2]
        if not idx in range(len(cards)):
            print("Index out of range")
            continue
        elif card in cards:
            print("Card is already bought")
        else:
            cards.insert(idx, card)
            print("Card successfully bought")


print(", ".join(cards))
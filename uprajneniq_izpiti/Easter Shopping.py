shops = input().split()
n = int(input())

for sh in range(n):
    data = input()
    command = data.split()[0]
    if command == "Include":
        shop = data.split()[1]
        shops.append(shop)
    elif command == "Visit":
        number_shop = int(data.split()[2])
        if not number_shop > len(shops):
            directions = data.split()[1]
            if directions == "first":
                for s in range(number_shop):
                    shops.pop(0)
            else:
                for s in range(number_shop):
                    shops.pop(-1)
    elif command == "Prefer":
        idx1 = int(data.split()[1])
        idx2 = int(data.split()[2])
        if idx2 in range(len(shops)) and idx1 in range(len(shops)):
            shop_ch1 = shops[idx1]
            shop_ch2 = shops.pop(idx2)
            shops.insert(idx2, shop_ch1)
            shops.pop(idx1)
            shops.insert(idx1, shop_ch2)
    elif command == "Place":
        idx = int(data.split()[2])
        if idx in range(len(shops)):
            shop = data.split()[1]
            shops.insert(idx + 1, shop)
print("Shops left:")
print(" ".join(shops))
n = int(input())

rarity = {}
rating = {}
counters = {}
for i in range(n):
    data = input().split("<->")
    plant = data[0]
    value = int(data[1])
    count = value

    rarity[plant] = count
    rating[plant] = 0
    counters[plant] = 0
while True:
    info = input()
    if info == "Exhibition":
        break
    info = info.split(": ")
    command = info[0]
    text = info[1].split(" - ")
    if command == "Rate":
        key = text[0]
        count = text[1]
        rating[key] += int(count)
        counters[key] += 1
    elif command == "Update":
        key = text[0]
        count = text[1]
        rarity[key] = count
    elif command == "Reset":
        key = text[0]
        rating[key] = 0
    else:
        print("error")
for k, v in rating.items():
    x = k
    if v == 0:
        counters[x] = 0
rarity_sorted = dict(sorted(rarity.items(), key=lambda x: x[1]))
print("Plants for the exhibition:")
for k, v in rating.items():
    y = counters[k]
    if y != 0:
        rating[k] = v / y
        print(f"- {k}; Rarity: {rarity_sorted[k]}; Rating: {rating[k]:.f2}")



# - {plant_name}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}

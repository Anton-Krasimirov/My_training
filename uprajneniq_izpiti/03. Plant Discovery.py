n = int(input())

plants = {}
# {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 7, 'rating': []}, 'Welwitschia': {'rarity': 2, 'rating': []}}
for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "rating": []}

input_data = input()
while not input_data == "Exhibition":
    comm, numms = input_data.split(": ")
    try:
        if comm == "Rate":
            plant, rating = numms.split(" - ")
            plants[plant]["rating"].append(int(rating))
        elif comm == "Update":
            plant, new_rarity = numms.split(" - ")
            plants[plant]["rarity"] = int(new_rarity)
        elif comm == "Reset":
            plant = numms
            plants[plant]["rating"].clear()
    except:
        print("error")
    input_data = input()
# {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 5, 'rating': [10, 5]}, 'Welwitschia': {'rarity': 2, 'rating': [7]}}
for k, v in plants.items():
    if plants[k]["rating"]:
        plants[k]["rating"] = sum(plants[k]["rating"]) / len(plants[k]["rating"])
    else:
        plants[k]["rating"] = 0
# {'Arnoldii': {'rarity': 4, 'rating': []}, 'Woodii': {'rarity': 5, 'rating': 7.5}, 'Welwitschia': {'rarity': 2, 'rating': 7.0}}

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]["rarity"], x[1]["rating"]), reverse=True)
# [('Woodii', {'rarity': 5, 'rating': 7.5}), ('Arnoldii', {'rarity': 4, 'rating': []}), ('Welwitschia', {'rarity': 2, 'rating': 7.0})]
print("Plants for the exhibition:")
for k, v in sorted_plants:
    print(f"- {k}; Rarity: {v['rarity']}; Rating: {v['rating']:.2f}")

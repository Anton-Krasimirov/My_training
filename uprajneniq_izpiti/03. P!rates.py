
cities = {}

text = input()
while text != "Sail":
    data = text.split("||")
    town = data[0]
    people = int(data[1])
    gold = int(data[2])
    if town not in cities:
        cities[town] = [people, gold]
    else:
        cities[town][0] += people
        cities[town][1] += gold
    text = input()

nexttodo = input()
while not nexttodo == "End":
    todo = nexttodo.split("=>")
    command = todo[0]
    town = todo[1]
    if command == "Plunder":
        people = int(todo[2])
        gold = int(todo[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            cities.pop(town)
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            print(f"{town} has been wiped off the map!")
            nexttodo = input()
            continue
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        nexttodo = input()
        continue
    elif command == "Prosper":
        gold = int(todo[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            nexttodo = input()
            continue
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
            nexttodo = input()
            continue

if len(cities) == 0:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
    exit()
else:
    cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for k, v in cities.items():
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")


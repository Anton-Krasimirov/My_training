peoples = {}

info = input()
while info != "Results":
    data = info.split(":")
    comm = data[0]
    if comm == "Add":
        name = data[1]
        health = int(data[2])
        energy = int(data[3])
        if not name in peoples:
            peoples[name] = {"health": health, "energy": energy}
        else:
            peoples[name]["health"] += health
    elif comm == "Attack":
        attak_name = data[1]
        defe_name = data[2]
        damage = int(data[3])
        if attak_name in peoples and defe_name in peoples:
            peoples[defe_name]["health"] -= damage
            peoples[attak_name]["energy"] -= 1
            if peoples[defe_name]["health"] <= 0 or peoples[defe_name]["energy"] == 0:
                peoples.pop(defe_name)
                print(f"{defe_name} was disqualified!")
            if peoples[attak_name]["health"] <= 0 or peoples[attak_name]["energy"] == 0:
                peoples.pop(attak_name)
                print(f"{attak_name} was disqualified!")
    elif comm == "Delete":
        name = data[1]
        if name == "All":
            peoples.clear()
        else:
            if name in peoples:
                del peoples[name]
    info = input()
peoples = dict(sorted(peoples.items(), key=lambda x: (-x[1]['health'], x[0])))
print(f"People count: {len(peoples)}")
for k, v in peoples.items():
    print(f"{k} - {v['health']} - {v['energy']}")
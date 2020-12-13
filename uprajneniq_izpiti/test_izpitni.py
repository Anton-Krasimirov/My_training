n = int(input())
heroes = {}

for _ in range(n):
    info = input().split()
    name = info[0]
    hp = int(info[1])
    mp = int(info[2])
    if name not in heroes:
        heroes[name] = {"hp": hp, "mp": mp}

data = input()
while data != "End":
    comm = data.split(" - ")[0]
    name = data.split(" - ")[1]
    if comm == "CastSpell":
        mp_needed = int(data.split(" - ")[2])
        spell_name = data.split(" - ")[3]
        if mp_needed <= heroes[name]["mp"]:
            heroes[name]["mp"] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mp']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif comm == "TakeDamage":
        damage = int(data.split(" - ")[2])
        attacker = data.split(" - ")[3]
        heroes[name]["hp"] -= damage
        if heroes[name]["hp"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hp']} HP left!")
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif comm == "Recharge":
        amount = int(data.split(" - ")[2])
        recovered = heroes[name]["mp"]
        heroes[name]["mp"] += amount
        if heroes[name]["mp"] > 200:
            heroes[name]["mp"] = 200
            recovered = 200 - recovered
            print(f"{name} recharged for {recovered} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")
    elif comm == "Heal":
        amount = int(data.split(" - ")[2])
        recovered = heroes[name]["hp"]
        heroes[name]["hp"] += amount
        if heroes[name]["hp"] > 100:
            heroes[name]["hp"] = 100
            recovered = 100 - recovered
            print(f"{name} healed for {recovered} HP!")
        else:
            print(f"{name} healed for {amount} HP!")
    data = input()

heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]['hp'], x[0])))
for k, v in heroes.items():
    print(k)
    print(f"  HP: {v['hp']}\n  MP: {v['mp']}")

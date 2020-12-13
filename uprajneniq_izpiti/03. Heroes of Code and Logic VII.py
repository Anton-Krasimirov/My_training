def castspel(dict, hero, m, spell):
    if dict[hero][1] >= m:
        dict[hero][1] -= m
        print(f"{hero} has successfully cast {spell} and now has {dict[hero][1]} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")
    return dict


def takedamage(dict, hero, h, attacker):
    dict[hero][0] -= h
    if dict[hero][0] > 0:
        print(f"{hero} was hit for {h} HP by {attacker} and now has {dict[hero][0]} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        dict.pop(hero)
    return dict


def recharge(dict, hero, m):
    n = dict[hero][1]
    dict[hero][1] += m
    if dict[hero][1] > 200:
        dict[hero][1] = 200
        m = 200 - n
    print(f"{hero} recharged for {m} MP!")
    return dict


def heal(dict, hero, h):
    n = dict[hero][0]
    dict[hero][0] += h
    if dict[hero][0] > 100:
        dict[hero][0] = 100
        h = 100 - n
    print(f"{hero} healed for {h} HP!")
    return dict

n = int(input())

heroes = {}

for i in range(n):
    text = input().split()
    name = text[0]
    hp = int(text[1])
    mp = int(text[2])
    heroes[name] = [hp, mp]

info = input()
while not info == "End":
    data = info.split(" - ")
    todo = data[0]
    name = data[1]
    if todo == "CastSpell":
        m = int(data[2])
        spell = data[3]
        heroes = castspel(heroes, name, m, spell)
    elif todo == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes = takedamage(heroes, name, damage, attacker)
    elif todo == "Recharge":
        amount = int(data[2])
        heroes = recharge(heroes, name, amount)
    elif todo == "Heal":
        amount = int(data[2])
        heroes = heal(heroes, name, amount)
    info = input()

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))
for k, v in sorted_heroes.items():
    print(k)
    print(f"  HP: {v[0]}")
    print(f"  MP: {v[1]}")
# ========================================================
# def cast_spell(heroes_dict, hero_name, mp_needed, spell_name):
#     current_mana_points = heroes_dict[hero_name]['MP']
#     if mp_needed > current_mana_points:
#         print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#     else:
#         heroes_dict[hero_name]['MP'] = (current_mana_points - mp_needed)
#         print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
#     return heroes_dict
#
#
# def take_damage(heroes_dict, hero_name, damage, attacker):
#     current_health_points = heroes_dict[hero_name]['HP']
#     healths_point_left = current_health_points - damage
#     if healths_point_left <= 0:
#         del heroes_dict[hero_name]
#         print(f"{hero_name} has been killed by {attacker}!")
#     else:
#         heroes_dict[hero_name]['HP'] = healths_point_left
#         print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {healths_point_left} HP left!")
#     return heroes_dict
#
#
# def recharge(heroes_dict, hero_name, amount):
#     current_mana_points = heroes_dict[hero_name]["MP"]
#     if current_mana_points + amount >= 200:
#         heroes_dict[hero_name]["MP"] = 200
#         print(f"{hero_name} recharged for {200- current_mana_points} MP!")
#     else:
#         heroes_dict[hero_name]["MP"] += amount
#         print(f"{hero_name} recharged for {amount} MP!")
#     return heroes_dict
#
#
# def heal(heroes_dict, hero_name, amount):
#     current_mana_points = heroes_dict[hero_name]["HP"]
#     if current_mana_points + amount >= 100:
#         heroes_dict[hero_name]["HP"] = 100
#         print(f"{hero_name} healed for {100- current_mana_points} HP!")
#     else:
#         heroes_dict[hero_name]["HP"] += amount
#         print(f"{hero_name} healed for {amount} HP!")
#     return heroes_dict
#
# heroes = {}
#
# n = int(input())
#
# for _ in range(n):
#     data = input().split(' ')
#     name = data[0]
#     hit_points = int(data[1])
#     mana_points = int(data[2])
#     heroes[name] = {"HP": hit_points, "MP": mana_points}
#
#
# command_data = input()
#
# while not command_data == "End":
#     command_data = command_data.split(" - ")
#     command = command_data[0]
#     if command == "CastSpell":
#         hero_name = command_data[1]
#         mp_needed = int(command_data[2])
#         spell_name = command_data[3]
#         heroes = cast_spell(heroes, hero_name, mp_needed, spell_name)
#     elif command == "TakeDamage":
#         hero_name, damage, attacker = command_data[1:]
#         damage = int(damage)
#         heroes = take_damage(heroes, hero_name, damage, attacker)
#     elif command == "Recharge":
#         hero_name = command_data[1]
#         amount = int(command_data[2])
#         heroes = recharge(heroes, hero_name, amount)
#     elif command == "Heal":
#         hero_name = command_data[1]
#         amount = int(command_data[2])
#         heroes = heal(heroes, hero_name, amount)
#     command_data = input()
#
#
# sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0]))
#
# for name, value in sorted_heroes:
#     print(name)
#     print(f"  HP: {value['HP']}")
#     print(f"  MP: {value['MP']}")

# ===============================================================
# number_of_heroes = int(input())
# heroes_data = {}
#
#
# def cast_spell(name, mana, spell, mana_availability):
#     if mana <= mana_availability:
#         mana_availability -= mana
#         print(f"{name} has successfully cast {spell} and now has {mana_availability} MP!")
#     else:
#         print(f"{name} does not have enough MP to cast {spell}!")
#     return mana_availability
#
#
# def take_dmg(name, dmg, attacker, health_availability):
#     health_availability[name]["HP"] -= dmg
#     if health_availability[name]["HP"] > 0:
#         print(f"{name} was hit for {dmg} HP by {attacker} and now has {health_availability[name]['HP']} HP left!")
#         return health_availability
#     else:
#         del health_availability[name]
#         print(f"{name} has been killed by {attacker}!")
#         return health_availability
#
#
# def recharge(name, mana, mana_availability):
#     needed_mana = 200-mana_availability
#     mana_availability += mana
#     if mana_availability >= 200:
#         mana_availability = 200
#         print(f"{name} recharged for {needed_mana} MP!")
#         return mana_availability
#     else:
#         print(f"{name} recharged for {mana} MP!")
#         return mana_availability
#
#
# def heal(name, health, health_availability):
#     needed_health = 100-health_availability
#     health_availability += health
#     if health_availability >= 100:
#         health_availability = 100
#         print(f"{name} healed for {needed_health} HP!")
#         return health_availability
#     else:
#         print(f"{name} healed for {health} HP!")
#         return health_availability
#
#
# for _ in range(number_of_heroes):
#     [hero_name, hp_points, mana_points] = input().split(" ")
#     hp_points = int(hp_points)
#     mana_points = int(mana_points)
#     heroes_data[hero_name] = {"HP": hp_points, "MP": mana_points}
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     action = command.split(" - ")
#     current_action = action[0]
#     current_name = action[1]
#     current_value = int(action[2])
#     if current_action == "CastSpell":
#         current_spell = action[3]
#         heroes_data[current_name]["MP"] = \
#             cast_spell(current_name, current_value, current_spell, heroes_data[current_name]["MP"])
#     elif current_action == "TakeDamage":
#         current_attacker = action[3]
#         heroes_data = \
#             take_dmg(current_name, current_value, current_attacker, heroes_data)
#     elif current_action == "Recharge":
#         heroes_data[current_name]["MP"] = \
#             recharge(current_name, current_value, heroes_data[current_name]["MP"])
#     elif current_action == "Heal":
#         heroes_data[current_name]["HP"] = \
#             heal(current_name, current_value, heroes_data[current_name]["HP"])
#
# filtered_heroes = sorted(heroes_data.items(), key=lambda x: (-x[1]["HP"], x[0]))
#
# for hero, data in filtered_heroes:
#     print(hero)
#     print(f"HP: {data['HP']}")
#     print(f"MP: {data['MP']}")


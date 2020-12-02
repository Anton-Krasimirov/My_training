import re

r_damege = r"([\+\-]?[0-9]+\.[0-9]+|[\+\-]?[0-9]+)"
r_health = r"[^\+\-\*\/\.\d]"

demons = [x.strip() for x in input().split(", ")]
demons.sort()
for demon in demons:
    demon = demon.replace(",", "")
    demon = demon.replace(" ", "")
    damage = re.findall(r_damege, demon)
    damage = sum(float(x) for x in damage)
    health = re.findall(r_health, demon)
    health = sum(ord(x) for x in health)
    for i in demon:
        if i == "*":
            damage *= 2
        elif i == "/":
            damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")

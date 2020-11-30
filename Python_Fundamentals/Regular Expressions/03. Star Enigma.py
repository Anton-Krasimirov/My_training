import re


def decode(text, x):
    decoded_text = ""
    for i in text:
        i = ord(i) - x
        i = chr(i)
        decoded_text += i
    return decoded_text


def find_idx(text):
    count = 0
    for i in text.lower():
        if i == "s" or i == "t" or i == "a" or i == "r":
            count += 1
    return count


n = int(input())

attacked_planets = {}

destroyed_planets = {}

check = r"([^\@\-\!\:\>]+)?@([A-Za-z]+)([^\@\-\!\:\>]+)?\:([\d]+)\!([A|D])!([^\@\-\!\:\>]+)?->([\d]+)([^\@\-\!\:\>]+)?"
a_count = 0
d_count = 0
for a in range(n):
    text = input()
    idx = find_idx(text)
    decoded_text = decode(text, idx)
    match = re.fullmatch(check, decoded_text)
    if match is None:
        continue
    planet_name = match[2]
    atack_type = match[5]
    if atack_type == "A":
        if planet_name not in attacked_planets:
            attacked_planets[planet_name] = 0
        attacked_planets[planet_name] += 1
    if atack_type == "D":
        if planet_name not in destroyed_planets:
            destroyed_planets[planet_name] = 0

        destroyed_planets[planet_name] += 1

print(f"Attacked planets: {len(attacked_planets)}")
for k, v in sorted(attacked_planets.items()):
    print(f"-> {k}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for k, v in sorted(destroyed_planets.items()):
    print(f"-> {k}")

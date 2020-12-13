import re
data = input()

pattern = r"(\#|\|)(?P<name>[A-Za-z\s]+)\1(?P<date>[\d+]{2}\/[\d+]{2}\/[\d+]{2})\1(?P<cal>[0-9][0-9]{0,3}|10000)\1"



info = re.finditer(pattern, data)
all_cal = 0
items = []

for x in info:
    products = x.groupdict()
    all_cal += int(products["cal"])
    items.append(products)


callories = all_cal // 2000

print(f"You have food to last you for: {callories} days!")
for x in items:
    print(f"Item: {x['name']}, Best before: {x['date']}, Nutrition: {x['cal']}")
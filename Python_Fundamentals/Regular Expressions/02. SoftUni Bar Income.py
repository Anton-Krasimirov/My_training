import re

check = r"^%([A-Z][a-z]+)%([^\|\$\%\.]+)?<([\w]+)>([^\|\$\%\.]+)?\|([0-9]+)\|([^\|\$\%\.\d]+)?([\d]+|[\d]+\.[\d]+)\$"

total_income = 0

data = input()
while not data == "end of shift":
    match = re.fullmatch(check, data)
    if match is None:
        data = input()
        continue

    name = match[1]
    product = match[3]
    count = int(match[5])
    prise = float(match[7])
    mid_income = count * prise
    total_income += mid_income
    print(f"{name}: {product} - {mid_income:.2f}")

    data = input()
print(f"Total income: {total_income:.2f}")

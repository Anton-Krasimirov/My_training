import re
pattern = r">>([A-Za-z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"
total_prise = 0
text = input()
print("Bought furniture:")
while text != "Purchase":
    match = re.fullmatch(pattern, text)
    if match is None:
        text = input()
        continue
    print(match[1])
    prise = float(match[2])
    quantity = int(match[4])
    total_prise += prise * quantity
    text = input()
print(f"Total money spend: {total_prise:.2f}")

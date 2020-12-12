import re
text = input()
destinations = []
counter = 0
regex = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"

result = re.finditer(regex, text, re.MULTILINE)


for i in result:
    res = i.group(2)
    counter += len(res)
    destinations.append(res)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {counter}")



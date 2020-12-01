import re
text = input()
destinations = []
counter = 0
regex = r"(=|/)([A-z][a-z]{2,})\1"

result = re.findall(regex, text)


for i in result:
    res = i[1]
    counter += len(res)
    destinations.append(res)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {counter}")



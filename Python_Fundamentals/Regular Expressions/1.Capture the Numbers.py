import re

pattern = r"\d+"
while True:
    text = input()
    if text == "":
        break
    res = re.findall(pattern, text)
    for r in res:
        print(r, end=" ")


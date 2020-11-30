import re

pattern = r"[w|W]{3}(\.[a-zA-Z0-9\-]+)+(\.[a-zA-Z]+)"
text = input()
while text != "":
    res = re.search(pattern, text)
    if res is None:
        text = input()
        continue
    print(res[0])
    text = input()

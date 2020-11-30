import re
text = input()
word = input()
pattern = rf"\b{word}\b"
res = re.findall(pattern, text, re.IGNORECASE)
print(len(res))


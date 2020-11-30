import re

text = input()
pattern = r"\b_([A-Za-z]+)\b"
res = re.finditer(pattern, text)
ress = []
for r in res:
    ress.append(r[1])

print(",".join(ress))

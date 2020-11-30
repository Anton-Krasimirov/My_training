import re

text = input()
pattern = r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b"

res = re.findall(pattern, text)
print(" ".join(res))

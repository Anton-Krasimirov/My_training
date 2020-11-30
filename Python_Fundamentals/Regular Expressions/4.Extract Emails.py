import re
user = r"(\s|^)[a-zA-Z0-9]+((\.|\-|\_)[a-zA-Z0-9]+)*"
host = r"[a-zA-z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"
text = input()
pattern = rf"{user}@{host}"
emails = re.finditer(pattern, text)
for mail in emails:
    print(mail[0])
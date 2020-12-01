import re
regex = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
text = input()
words = []
matches = re.findall(regex, text)
for m in matches:
    first = m[1]
    second = m[2]
    if first == second[::-1]:
        words.append(first + " <=> " + second)

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if len(words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(words))
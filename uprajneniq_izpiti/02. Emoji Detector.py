import re


r_digit = r"\d"
r_emoji = r"((::|\*\*)([A-Z][a-z]{2,})\2)"

text = input()

digits = re.findall(r_digit, text)
digits = [int(x) for x in digits]
cool = digits[0]
for i in digits[1:]:
    cool *= i
emoji = {}
em_ji = re.findall(r_emoji, text)
for i in em_ji:
    key = i[0]
    val = sum([ord(x) for x in i[2]])
    emoji[key] = val



print(f"Cool threshold: {cool}")
print(f"{len(emoji)} emojis found in the text. The cool ones are:")
for k, v in emoji.items():
    if v >= cool:
        print(k)

line = input()

text = input()
while line in text:
    text = text.replace(line, "")

print(text)

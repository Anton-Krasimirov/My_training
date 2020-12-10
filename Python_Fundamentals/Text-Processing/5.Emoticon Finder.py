text = input()

for i in range(len(text)):
    ch = text[i]
    if ch == ':' and text[i+1] != " ":
        simbol = text[i+1]
        print(f'{ch}{simbol}')



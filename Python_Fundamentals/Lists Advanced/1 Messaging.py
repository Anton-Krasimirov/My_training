list_num = input().split(" ")
text = list(input())
result = ""
number = []
numb = 0
for i in list_num:
    num = i
    for n in num:
        x = int(n)
        numb += x
    number.append(numb)
    numb = 0
for n in number:
    if n > len(text):
        n = n - len(text)
    result += text[n]
    text.pop(n)
print(result)
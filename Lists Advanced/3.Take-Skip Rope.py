in_text = [n for n in input()]
result = []
x_text = []
numbers = []
take_list = []
skip_list = []
for ch in in_text:
    if ch.isdigit():
        numbers.append(int(ch))
    else:
        x_text.append(ch)

for i, v in enumerate(numbers):
    if i % 2 == 0:
        take_list.append(v)
    else:
        skip_list.append(v)
for i, t in enumerate(take_list):
    pease = x_text[:t]
    result.append(pease)
    x_text = x_text[t:]
    b = skip_list[i]
    if b == 0:
        continue
    x_text = x_text[b:]

for i in result:
    print("".join(i), end="")

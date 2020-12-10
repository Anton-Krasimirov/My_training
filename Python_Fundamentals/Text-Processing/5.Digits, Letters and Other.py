text = input()

num = ""
alpha = ""
other = ""

for i in text:
    if i.isdigit():
        num += i
    elif i.isalpha():
        alpha += i
    else:
        other += i

print(f'{num}\n{alpha}\n{other}\n')
# print(num)
# print(alpha)
# print(other)
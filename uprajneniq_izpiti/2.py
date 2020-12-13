import re
n = int(input())

info = []
for _ in range(n):
    data = input()
    info.append(data)



reger = r"(\*|@)([A-Z][a-z]{2,})\1(\: )(\[[A-Za-z]\]\|\[[a-z]\]\|\[[a-z]\]\|)$"

for i in info:
    x = re.findall(reger, i)
    if not x == []:
        sum = []
        name = x[0][1]
        nums = x[0][3]
        for alph in nums:
            if alph.isalpha():
                alph = ord(alph)
                sum.append(str(alph))
        print(f"{name}: {' '.join(sum)}")
    else:
        print("Valid message not found!")


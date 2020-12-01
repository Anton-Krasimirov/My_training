list = [int(x) for x in input().split()]

y = 0

top_five = []

for x in list:
    y += x
average = y / len(list)

top_num = [x for x in list if x > average]
if len(top_num) < 5:
    for x in top_num[:len(top_num) + 1:]:
        a = max(top_num)
        top_five.append(a)
        top_num.remove(a)
else:
    for x in top_num[:5:]:
        a = max(top_num)
        top_five.append(a)
        top_num.remove(a)
if len(list) < 3:
    print("No")
else:
    print(top_five)

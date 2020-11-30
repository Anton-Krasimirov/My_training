import re

rname = r"[A-Za-z]"
rpoints = r"\d"
list_name = input().split(", ")
rang_list = {}

row = input()
while row != "end of race":
    n = re.findall(rname, row)
    p = re.findall(rpoints, row)
    name = "".join(w for w in n)
    points = sum(int(x) for x in p)
    if name in list_name:
        if name not in rang_list:
            rang_list[name] = points
        else:
            rang_list[name] += points
    row = input()
rang_list_sort = dict(sorted(rang_list.items(), key=lambda x: -x[1]))
rang = []
for key in rang_list_sort.keys():
    rang.append(key)

print(f"1st place: {rang[0]}\n2nd place: {rang[1]}\n3rd place: {rang[2]}\n")

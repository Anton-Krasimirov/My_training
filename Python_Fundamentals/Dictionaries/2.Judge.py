constests = {}
name_points = {}

data = input()

while True:
    if data == "no more time":
        break
    username, constest, points = data.split(" -> ")
    points = int(points)
    if constest not in constests:
        constests[constest] = {username: points}

    else:
        if username not in constests[constest]:
            constests[constest][username] = points
        else:
            if points > constests[constest][username]:
                dif = constests[constest][username]
                constests[constest][username] = points
                name_points[username] -= dif
    if username not in name_points:
        name_points[username] = points
    else:
        name_points[username] += points

    data = input()

sort_name_points = dict(sorted(name_points.items(), key=lambda x: (-x[1], x[0])))

keys = [k for k in constests.keys()]
values = [v for v in constests.values()]
dict_val = [dict(sorted(x.items(), key=lambda kv: (-kv[1], kv[0]))) for x in values]

sort_constents = dict(zip(keys, dict_val))

for key, val in sort_constents.items():
    print(f"{key}: {len(val)} participants")
    count = 1
    for v in val.items():
        print(f"{count}. {v[0]} <::> {v[1]}")
        count += 1
print("Individual standings:")
count = 1
for key, val in sort_name_points.items():
    print(f"{count}. {key} -> {val}")
    count += 1

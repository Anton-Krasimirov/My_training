content_pass = {}
user_cours_points = {}

while True:
    data_content = input()
    if data_content == "end of contests":
        break
    data = data_content.split(":")
    cours = data[0]
    pass_word = data[1]

    content_pass[cours] = pass_word

while True:
    next_data = input()
    if next_data == "end of submissions":
        break
    content, password, username, points = next_data.split("=>")
    points = int(points)
    if content in content_pass and password == content_pass[content]:
        if username not in user_cours_points:
            user_cours_points[username] = {content: points}
        else:
            if content in user_cours_points[username].keys():
                if user_cours_points[username][content] < points:
                    user_cours_points[username][content] = points
            else:
                user_cours_points[username][content] = points

user_cours_points = dict(sorted(user_cours_points.items(), key=lambda x: x[0]))
keys = [k for k in user_cours_points.keys()]
print(keys)
dict_value = [v for v in user_cours_points.values()]
print(dict_value)
dict_values = [dict(sorted(x.items(), key=lambda kv: kv[1], reverse=True)) for x in dict_value]
print(dict_values)
nesteddict = dict(zip(keys, dict_values))
print(nesteddict)
max_points = 0
user = ""
for k, val in nesteddict.items():
    point_s = 0
    for v in val.values():
        point_s += v
    if max_points < point_s:
        max_points = point_s
        user = k

print(f"Best candidate is {user} with total {max_points} points.")
print("Ranking:")
for k, v in nesteddict.items():
    print(k)
    for n in v:
        print(f"#  {n} -> {v[n]}")

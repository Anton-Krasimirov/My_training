name_cours = {}
name_points = {}
banned = []

list = input()
while list != "exam finished":
    args = list.split("-")
    if len(args) == 2:
        name = args[0]
        banned.append(name)
    else:
        name = args[0]
        cours = args[1]
        points = int(args[2])
        if name not in name_cours:
            name_cours[name] = []
        name_cours[name].append(cours)

        if name not in name_points:
            name_points[name] = []
        name_points[name].append(points)

    list = input()


name_points = dict(sorted(name_points.items(), key=lambda x: (-max(x[1]), x[0])))
print(f"Results:")
for name, points in name_points.items():
    if name not in banned:
        print(f'{name} | {max(points)}')

print("Submissions:")
new_dict = []
total = {}

for key, value in name_cours.items():
    new_dict += value
for _ in new_dict:
    neme = _
    num = new_dict.count(_)
    if neme not in total:
        total[neme] = num
total = dict(sorted(total.items(), key=lambda x: (-x[1], x[0])))
for key, value in total.items():
    print(f'{key} - {value}')

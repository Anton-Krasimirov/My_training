infomation = input()

courses = {}

while infomation != "end":
    args = infomation.split(' : ')
    cours  = args[0]
    st_name = args[1]

    if cours not in courses:
        courses[cours] = []

    courses[cours].append(st_name)
    infomation = input()

courses_sort = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for key, value in courses_sort.items():
    print(f'{key}: {len(value)}')
    for st_name in sorted(value):
        print(f'-- {st_name}')









companies = {}

info = input()

while info != 'End':
    data = info.split(' -> ')
    name = data[0]
    id = data[1]

    if name not in companies:
        companies[name] = []
        if not id in companies[name]:
            companies[name].append(id)
    else:
        if not id in companies[name]:
            companies[name].append(id)

    info = input()


for (name, id) in sorted(companies.items()):
    print(f'{name}')
    for i in range(0, len(id)):
        print(f'-- {"".join(id[i])}')


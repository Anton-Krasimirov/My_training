from sys import maxsize


def get_max(d: dict):
    entries = d.items()
    max_name = ''
    total_points = - maxsize
    for entry in entries:
        if entry[1][1] > total_points:
            max_name = entry[0]
            total_points = entry[1][1]
    return max_name, total_points


line = input()
contests = {}

while not line == 'end of contests':
    data = line.split(':')
    contest = data[0]
    password = data[1]
    contests[contest] = password
    line = input()

line = input()
results = {}

while not line == 'end of submissions':
    data = line.split('=>')
    contest = data[0]
    password = data[1]
    username = data[2]
    points = int(data[3])
    if contest in contests.keys():
        if contests[contest] == password:
            if username in results.keys():
                if contest in results[username].keys():
                    if points > results[username][contest]:
                        results[username][contest] = points
                else:
                    results[username][contest] = points
            else:
                results[username] = {contest: points}
    line = input()

for username in results.keys():
    total = sum(results.get(username).values())
    results[username] = [results[username], total]
    results[username][0] = dict(sorted(results.get(username)[0].items(), key=lambda x: x[1], reverse=True))

results = dict(sorted(results.items(), key=lambda x: x[0]))
name, result = get_max(results)
print(f'Best candidate is {name} with total {result} points.')
print('Ranking:')
for res in results.items():
    print(res[0])
    for contest in res[1][0].items():
        print(f'#  {contest[0]} -> {contest[1]}')
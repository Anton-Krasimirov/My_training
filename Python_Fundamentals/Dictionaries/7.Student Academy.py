n = int(input())

stud_grade = {}

for i in range(n):
    name = str(input())
    grade = float(input())

    if name not in stud_grade:
        stud_grade[name] = []

    stud_grade[name].append(grade)

new_dict = {}
for name, grade in stud_grade.items():
    value = sum(grade) / len(grade)
    if value >= 4.50:
        new_dict[name] = value

new_dict = dict(sorted(new_dict.items(), key=lambda x: -x[1]))

for name, value in new_dict.items():
    print(f'{name} -> {value:.2f}')


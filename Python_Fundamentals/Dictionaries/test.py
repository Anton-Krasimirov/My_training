


name_skill = {'Pesho': {'Adc': 400}, 'Bush': {'Tank': 150, 'Abc': 100, 'Crt': 120}, 'Faker': {'Mid': 200, 'Support': 250, 'Tank': 250}}

a = 7

plauer1 = name_skill['Faker'].keys()
player2 = name_skill['Bush'].keys()

for x in plauer1:
    for y in player2:
        if x == y:
            if int(name_skill['Faker'][x]) > int(name_skill['Bush'][y]):
                name_skill.pop('Bush')
                break
            else:
                name_skill.pop('Faker')
                break
print(name_skill)
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
count = ""
while count == "":
    text = input().lower().split()
    for i in range(0, len(text), 2):
        num = int(text[i])
        key = text[i + 1]
        if key in key_materials:
            key_materials[key] += num
            if key_materials[key] >= 250:
                count = key
                key_materials[key] -= 250
                if count == 'shards':
                    print('Shadowmourne obtained!')
                elif count == 'fragments':
                    print("Valanyr obtained!")
                elif count == 'motes':
                    print("Dragonwrath obtained!")
                key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
                junk = dict(sorted(junk.items(), key=lambda x: x[0]))
                for key, value in key_materials.items():
                    print(f'{key}: {value}')
                for key, value in junk.items():
                    print(f'{key}: {value}')
                exit()
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += num














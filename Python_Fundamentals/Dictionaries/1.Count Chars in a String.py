text = input()


letters = [letter for letter in text if letter != " "]

sumbols = {}

for sumbol in letters:
    if sumbol not in sumbols:
        sumbols[sumbol] = 0

    sumbols[sumbol] += 1

for key, value in sumbols.items():


    print(f"{key} -> {value}")
data = input()
all_constest = {}
individual_points = {}
while True:
    if data == "no more time":
        break
    split_data = data.split(" -> ")
    constest = split_data[1]
    username = split_data[0]
    points = int(split_data[2])
    if constest not in all_constest:
        all_constest[constest] = {username: points}
    else:
        if username not in all_constest[constest]:
            all_constest[constest][username] = points
        else:
            if points > all_constest[constest][username]:
                all_constest[constest][username] = points
    if username not in individual_points:
        individual_points[username] = points
    else:
        individual_points[username] += points
    data = input()



print(all_constest)
print(individual_points)
peoples = int(input())
PLASE = 4
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    while not lift[i] == PLASE:
        if peoples > 0:
            peoples -= 1
            lift[i] += 1
        else:
            break

all_seats = len(lift) * PLASE
fill_seats = sum(lift)

if peoples == 0 and fill_seats < all_seats:
    print(f"The lift has empty spots!")
else:
    if peoples > 0 and fill_seats == all_seats:
        print(f"There isn't enough space! {peoples} people in a queue!")
print(' '.join([str(x) for x in lift]))
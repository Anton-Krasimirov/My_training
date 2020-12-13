first = int(input())
second = int(input())
third = int(input())

capasiti_hour = first + second + third

peoples = int(input())
count_hours = 0
while peoples > 0:
    peoples -= capasiti_hour
    count_hours += 1
    if count_hours % 4 == 0:
        count_hours += 1

print(f"Time needed: {count_hours}h.")
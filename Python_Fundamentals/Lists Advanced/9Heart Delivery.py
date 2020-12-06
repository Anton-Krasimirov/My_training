neighborhood = [int(x) for x in input().split("@")]

current_index = 0
counter = []
data = input()
while not data == "Love!":
    jump = int(data.split()[1])
    current_index += jump
    if current_index + 1 > len(neighborhood):
        current_index = 0
    if current_index in counter and neighborhood[current_index] <= 0:
        print(f"Place {current_index} already had Valentine's day.")
        data = input()
        continue
    neighborhood[current_index] -= 2
    if neighborhood[current_index] <= 0:
        print(f"Place {current_index} has Valentine's day.")
        counter.append(current_index)

    data = input()
print(f"Cupid's last position was {current_index}.")
count_house = [x for x in neighborhood if x != 0]
if not count_house:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(count_house)} places.")




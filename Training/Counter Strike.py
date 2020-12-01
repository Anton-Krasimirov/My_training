power = int(input())

counter = 0
data = input()
while not data == "End of battle":
    data = int(data)
    if (power - data) < 0:
        print(f'Not enough energy! Game ends with {counter} won battles and {power} energy')
        exit()
    power -= data
    counter += 1
    if counter % 3 == 0:
        power += counter
    data = input()


print(f"Won battles: {counter}. Energy left: {power}")

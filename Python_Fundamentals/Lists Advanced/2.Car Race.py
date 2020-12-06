elements = [int(n) for n in input().split()]

car_value = len(elements) // 2
final_value = int(elements[car_value])

left = 0
right = 0

for idx in elements[-1: car_value: -1]:
    right += idx
    if idx == 0:
        right *= 0.8

for b in elements[:car_value]:
        left += b
        if b == 0:
            left *= 0.8

if left > right:
    print(f"The winner is right with total time: {right:.1f}")
else:
    print(f"The winner is left with total time: {left:.1f}")
from collections import deque


quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
while orders:
    num = orders.popleft()
    if num <= quantity:
        quantity -= num
    else:
        orders.appendleft(num)
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:

    print("Orders complete")

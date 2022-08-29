cables = [int(x) for x in input().split()]
size = len(cables) + 1

positions = [pos for pos in range(1, size)]

lcs = []

[lcs.append([0] * size) for _ in range(size)]

# [2, 5, 3, 8, 7, 4, 6, 9, 1]--cables
# [1, 2, 3, 4, 5, 6, 7, 8, 9]--positions

for row in range(1, size):# 0
    for col in range(1, size): # 0, 1, 2, 3
        if cables[row - 1] == positions[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])

print(f'Maximum pairs connected: {lcs[size - 1][size - 1]}')
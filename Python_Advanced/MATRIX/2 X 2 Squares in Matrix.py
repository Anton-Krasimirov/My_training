r, c = [int(x) for x in input().split()]

matrix = []
counter = 0
for i in range(r):
    data = [x for x in input().split()]
    matrix.append(data)

for row in range(len(matrix) - 1):
    for col in range(c - 1):
        idx = matrix[row][col]
        if idx == matrix[row][col + 1] and idx == matrix[row + 1][col] and idx == matrix[row + 1][col + 1]:
            counter += 1

print(counter)
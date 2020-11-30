count_rows = int(input())

matrix = []

for i in range(count_rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

sum_diagonal = 0
for i in range(count_rows):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
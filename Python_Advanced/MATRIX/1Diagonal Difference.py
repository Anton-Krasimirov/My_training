n = int(input())

matrix = []

for i in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

diagonal1 = 0
diagonal2 = 0


for i in range(len(matrix)):
    num = matrix[i][i]
    diagonal1 += num
a = 5
for i in range(len(matrix)):
    num = matrix[i][n - i - 1]
    diagonal2 += num

diference = abs(diagonal1 - diagonal2)
print(diference)
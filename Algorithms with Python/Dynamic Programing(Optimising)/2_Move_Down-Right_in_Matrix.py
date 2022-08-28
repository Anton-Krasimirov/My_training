from collections import deque
rows = int(input())
cols = int(input())

matrix = []
dp = [] # тук ще държим сумите на стойностите от горната матрица

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols) # правим ред от нули в другата матрица

dp[0][0]= matrix[0][0] # първаат стойност не се променя
# input :
#8
#7
# 2 6 1 8 9 4 2
# 1 8 0 3 5 6 7
# 3 4 8 7 2 1 8
# 0 9 2 8 1 7 9
# 2 7 1 9 7 8 2
# 4 5 6 1 2 5 6
# 9 3 5 2 8 1 9
# 2 3 4 1 7 2 8

for col in range(1, cols): # ще се движим по реда на дясно , до края
    dp[0][col] = dp[0][col - 1] + matrix[0][col]# започваме от втора позиция или индекс 1

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]
# [[2, 8, 9, 17, 26, 30, 32],
#   [3, 0, 0, 0, 0, 0, 0],
#   [6, 0, 0, 0, 0, 0, 0],
#   [6, 0, 0, 0, 0, 0, 0],
#   [8, 0, 0, 0, 0, 0, 0],
#   [12, 0, 0, 0, 0, 0, 0],
#   [21, 0, 0, 0, 0, 0, 0],
#   [23, 0, 0, 0, 0, 0, 0]]
for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col] # по-голямата сума между горния ред същата колона или същия ред
        # предната колона + числото от настоящата позиция в началната матрица

# [[2, 8, 9, 17, 26, 30, 32],
#  [3, 16, 16, 20, 31, 37, 44],
#  [6, 20, 28, 35, 37, 38, 52],
#  [6, 29, 31, 43, 44, 51, 61],
#  [8, 36, 37, 52, 59, 67, 69],
#  [12, 41, 47, 53, 61, 72, 78],
#  [21, 44, 52, 55, 69, 73, 87],
#  [23, 47, 56, 57, 76, 78, 95]]

# позицията от която ще тръгнем на обратно
row = rows - 1
col = cols - 1
result = deque()
while row > 0 and col > 0:
    result.appendleft([row, col]) # добавяме пътя по който минаваме в опашката
    if dp[row][col -1] >= dp[row - 1][col]:# >= и приотизирането трябва да е обратното, на избора на слизане към последната позиция
        col -= 1
    else:
        row -= 1

while row > 0:
    result.appendleft([row, col])
    row -= 1
while col > 0:
    result.appendleft([row, col])
    col -= 1
result.appendleft([0, 0])
print(*result, sep=' ')
first = input() # tree
second = input() # # team

rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]
#  [0, 0, 0, 0, 0] ----[0, 0, 0, 0, 0]--първите ред и колона не ги гледаме
#  [0, 0, 0, 0, 0] ----[0, 1, 1, 1, 1]
#  [0, 0, 0, 0, 0] ----[0, 1, 1, 1, 1]
#  [0, 0, 0, 0, 0] ----[0, 1, 2, 2, 2]
#  [0, 0, 0, 0, 0] ----[0, 1, 2, 2, 2]

for row in range(1, rows):
    for col in range(1, cols): # tree --- # team
        if first[row - 1] == second[col - 1]:# (0, 0) (0, 1) (0, 2) (0, 3)
            dp[row][col] = dp[row - 1][col - 1] + 1 # ляв горен диагонал стойноста му + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) # по-голямата стойност от едно на ляво или едно на горе

print(dp[rows - 1][cols - 1])
# for row in dp:
#     print(row)
#=================== ако искам да изведа съвпадащите елементи :
row = rows - 1
col = cols - 1
result = []

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.append(first[row - 1]) # или second[col - 1]
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(list(reversed(result)))
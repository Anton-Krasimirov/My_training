'''две матрици , едната е като вход , другата съдържа обходените позиции, един каунтър за общ брой ерии, един речник за всички ерии'''
def dfs(parent, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):# проверка дали сме в матрицата
        return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:# рзличен символ
        return


    visited[row][col] = True
    dfs(parent, row - 1, col, matrix, visited)
    dfs(parent, row + 1, col, matrix, visited)
    dfs(parent, row, col - 1, matrix, visited)
    dfs(parent, row, col + 1, matrix, visited)

rows = int(input())
cols = int(input())

matrix = []
visited = []# държи обходените позиции , за да не се дублират някъде

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0
for row in range(rows):
    for col in range(cols):
        if visited[row][col]:# игнорираме защото е част от обхожданите и не търсим започвайки от нея
            continue
        key = matrix[row][col]# взимаме го за да сравним дали е съседна клетка
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1


print(f"Areas: {total_areas}")
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> {size}")
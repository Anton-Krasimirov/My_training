def made_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([x for x in input()])
    return matrix


def is_valid(current_pos, n):
    r = current_pos[0]
    c = current_pos[1]
    return 0 <= r < n and 0 <= c < n


def get_position(row, col, n, matrix):
    count_to_kill = 0
    row_pos = [+ 1, - 1, - 1, + 1, - 2, - 2, + 2, + 2]
    col_pos = [+ 2, + 2, - 2, - 2, - 1, + 1, - 1, + 1]
    for i in range(8):
        current_pos = [row + row_pos[i], col + col_pos[i]]
        if is_valid(current_pos, n) and matrix[current_pos[0]][current_pos[1]] == "K":
            count_to_kill += 1
    return count_to_kill


n = int(input())
matrix = made_matrix(n)
total_kills = 0

while True:
    count_for_removed = 0
    positions = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "K":
                num_get_posible = get_position(row, col, n, matrix)
                if count_for_removed < num_get_posible:
                    count_for_removed = num_get_posible
                    positions = [row, col]

    if count_for_removed == 0:
        break

    kill_row = positions[0]
    kill_col = positions[1]
    matrix[kill_row][kill_col] = "0"
    total_kills += 1

print(total_kills)


# matrix = [
#       0  1  2  3  4
#     0[0, 1, 2, 3, 4],
#     1[0, 1, 2, 3, 4],
#     2[0, 1, 2, 3, 4],
#     3[0, 1, 2, 3, 4],
#     4[0, 1, 2, 3, 4],
# ]
# ( ), ( ), ( ), ( ), ( ), ( ), (( )), ( )
# row i + 1, i - 1, i - 1, i + 1, i - 2, i - 2, i + 2, i + 2,
# col i + 2, i + 2, i - 2, i - 2, i - 1, i + 1, i - 1, i + 1,

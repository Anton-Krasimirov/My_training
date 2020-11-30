n = int(input())
matrix = [[x for x in input()]for i in range(n)]


row_pos = [+ 1, - 1, - 1, + 1, - 2, - 2, + 2, + 2]
col_pos = [+ 2, + 2, - 2, - 2, - 1, + 1, - 1, + 1]
for i in range(8):
    current_pos = [row + row_pos[i], col + col_pos[i]]


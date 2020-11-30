matrix = [
    [7, 1, 3, 3, 2, 1],
    [1, 3, 9, 8, 5, 6],
    [4, 6, 7, 9, 1, 0],
    [9, 4, 5, 3, 2, 2],
    [8, 3, 3, 5, 1, 0],
]
x = len(matrix)
v = len(matrix[0])
new_matrix = []
bestsum = -9999999

for row in range(x - 3):# do koi red nadolu
    for col in range(v - 3):# na vatre v reda
        submatrix = []
        start = 0# pri vtoriq cikal da mine na sledvashtata kolona
        currentsum = 0
        for r in range(row, row + 4):# opredelq ednata strana na kvadrata
            submatrix.append([])
            for c in range(col, col + 4):# opredelq vtorata strana na kvadrata
                submatrix[start].append(matrix[r][c])# kade da postavq chislata
                currentsum += matrix[r][c]
            start += 1
        if currentsum > bestsum:
            new_matrix = submatrix
            bestsum = currentsum
# matrix = [
#       0  1  2  3  4
#     0[0, 1, 2, 3, 4],
#     1[0, 1, 2, 3, 4],
#     2[0, 1, 2, 3, 4],
#     3[0, 1, 2, 3, 4],
#     4[0, 1, 2, 3, 4],
# ]


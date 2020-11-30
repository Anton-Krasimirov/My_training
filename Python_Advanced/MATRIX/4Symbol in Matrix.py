def check_matrix_search(matrix, search):
    for rows in range(len(matrix)):
        row = matrix[rows]
        for column in range(len(row)):
            if search == matrix[rows][column]:
                return rows, column

    return f"{search} does not occur in the matrix"


n = int(input())
matrix = []
for _ in range(n):
    row = [x for x in input()]
    matrix.append(row)

simbol = input()

print(check_matrix_search(matrix, simbol))

# rows_count = int(input())
# matrix = [list(n for n in input()) for _ in range(rows_count)]
# symbol = input()
# is_symbol_in = False
# row = ""
# index = ""
# for row in range(rows_count):
#     symbols = matrix[row]
#     for index, symb in enumerate(symbols):
#         if symb == symbol:
#             is_symbol_in = True
#             break
#     if is_symbol_in:
#         break
#
# if is_symbol_in:
#     print(f"({row}, {index})")
# else:
#     print(f"{symbol} does not occur in the matrix")

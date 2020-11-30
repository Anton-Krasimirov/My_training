# rows, columns = [int(x) for x in input().split(", ")]
# #
# # matrix = []
# # for i in range(rows):
# #     row = [int(x) for x in input().split()]
# #     matrix.append(row)
# #
# # for j in range(columns):
# #     count = 0
# #     for row in matrix:
# #         value = row[j]
# #         count += value
# #     print(count)

def read_int_list_input(separator=" "):
    return [int(x) for x in input().split(separator)]

(rows, columns) = read_int_list_input(", ")
matrix = []

for i in range(rows):
    matrix.append(read_int_list_input())

count_columns = [0] * columns

for row in range(rows):
    for column in range(columns):
        count_columns[column] += matrix[row][column]

[print(x) for x in count_columns]
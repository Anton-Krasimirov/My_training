rows, columns = [int(x) for x in input().split(", ")]

matrix = []
value = 0

for i in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    value += sum(row)

print(value)
print(matrix)

# rows, columns = [int(x) for x in input().split(", ")]
#
# matrix = []
#
# for i in range(rows):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#
#
# print(sum(sum(row) for row in matrix))
# print(matrix)

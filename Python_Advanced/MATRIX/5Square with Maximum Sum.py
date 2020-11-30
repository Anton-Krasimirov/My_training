from itertools import chain

def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = [[int(x) for x in input().split(", ")]for _ in range(row)]
    return matrix


def get_square(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
            squares.append(square)
    return squares


def get_sum_square(matrix):# ще се подават подматриците, квадратите
    return sum(chain(*matrix))# сумата на всички редове в матрицата, подредени за обхождане

def max_square(squares):
    max_square_sum = None
    max_square = None
    for square in squares:
        sum_square = get_sum_square(square)
        if max_square_sum is None or sum_square > max_square_sum:
            max_square_sum = sum_square
            max_square = square
    return max_square

matrix = read_matrix()
squares = get_square(matrix)
max_square = max_square(squares)
print("\n".join([" ".join(map(str, row))for row in max_square]))
print(get_sum_square(max_square))

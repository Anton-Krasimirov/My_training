def make_matrix(r):
    matrix = []
    for _ in range(r):
        matrix.append(input().split())
    return matrix


def change_matrix(info, a, b, c, d):
    pos1 = info[a][b]
    pos2 = info[c][d]
    info[a][b] = pos2
    info[c][d] = pos1
    return info


def check_valid(a, b):
    if row > a >= 0 and 0 <= b < col:
        return True


row, col = [int(x) for x in input().split()]
matrix = make_matrix(row)
data = input()
while not data == "END":
    data = data.split()
    if not len(data) == 5 or not data[0] == "swap":
        print("Invalid input!")
        data = input()
        continue
    r1 = int(data[1])
    c1 = int(data[2])
    r2 = int(data[3])
    c2 = int(data[4])
    if check_valid(r1, c1) and check_valid(r2, c2):
        matrix = change_matrix(matrix, r1, c1, r2, c2)
        for r in matrix:
            print(" ".join(str(x) for x in r))
    else:
        print("Invalid input!")

    data = input()

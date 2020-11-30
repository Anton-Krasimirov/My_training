r, c = [int(x) for x in input().split()]

matrix = []
counter = 0
for i in range(r):
    data = [int(x) for x in input().split()]
    matrix.append(data)

biggest_cube = []
biggest_sum = -9999

sub_cube = []
cube_sum = 0
for x in range(r - 2):
    for y in range(c - 2):
        line_sub_cube = []
        for row in range(x, x + 3):
            a = 5
            for col in range(y, y + 3):
                line_sub_cube.append(matrix[row][col])
            sub_cube.append(line_sub_cube)
            midle_sum = sum(line_sub_cube)
            cube_sum += midle_sum
            line_sub_cube = []
        if cube_sum > biggest_sum:
            biggest_sum = cube_sum
            biggest_cube = sub_cube
            sub_cube = []
            cube_sum = 0
        else:
            sub_cube = []
            cube_sum = 0


print(f"Sum = {biggest_sum}")
for i in range(len(biggest_cube)):
    print(" ".join(str(x) for x in biggest_cube[i]))






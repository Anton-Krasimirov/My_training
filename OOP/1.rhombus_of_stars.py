def generate_line(idx, n):
    ident = ' ' * (n - idx - 1)
    stars = '* ' * (idx + 1)
    return f'{ident}{stars}'


def print_rhombus(n):
    for i in range(n):
        print(generate_line(i, n))

    for i in range(n - 2, -1, -1):
        print(generate_line(i, n))


n = int(input())
print_rhombus(n)
def sum_numbers(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def add_subtract(n1, n2, n3):
    result = sum_numbers(n1, n2)
    print(subtract(result, n3))

n1 = int(input())
n2 = int(input())
n3 = int(input())

add_subtract(n1, n2, n3)


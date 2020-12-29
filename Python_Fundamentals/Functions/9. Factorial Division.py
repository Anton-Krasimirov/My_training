num1 = int(input())
num2 = int(input())


def factorial_of_number():
    n1 = 1
    n2 = 1

    for i in range(num1, 0 + 1, -1):
        n1 *= i

    for i in range(num2, 0 + 1, -1):
            n2 *= i

    n3 = n1 / n2

    print(f"{n3:.2f}")


factorial_of_number()

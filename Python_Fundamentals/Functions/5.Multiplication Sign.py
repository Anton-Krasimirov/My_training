def multiplication(a, b, c,):
    if a < 0 or b < 0 or c < 0:
        return "negative"
    if a > 0 and b > 0 and c > 0:
        return "positive"
    if a == 0 or b == 0 or c == 0:
        return "zero"


num = int(input())
num1 = int(input())
num2 = int(input())

print(multiplication(num, num1, num2))


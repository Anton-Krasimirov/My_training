operation = input()
a = int(input())
b = int(input())

def perform_opreration(a, b, operation):
    if operation == 'add':
        return a + b
    if operation == 'subtract':
        return a - b
    if operation == 'divide':
        return int(a / b)
    if operation == 'multiply':
        return a * b

print(perform_opreration(a, b, operation))

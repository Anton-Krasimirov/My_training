text = input().split()

stack = []

while text:
    stack.append(text.pop())

print(" ".join(stack))


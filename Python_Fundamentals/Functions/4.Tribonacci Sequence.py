def tribonacci(n):
    start = [1, 1, 2]
    for i in range(1, n):
        if i >= 3:
            x = start[-1]  + start[-2] + start[-3]
            start.append(x)
    return start


num = int(input())

print(tribonacci(num))


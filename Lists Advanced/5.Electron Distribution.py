n = int(input())

count = []
shield = 1
while n > 0:
    value = 2 * shield ** 2
    if n > value:
        count.append(value)
        shield += 1
        n -= value
    else:
        count.append(n)
        break

print(count)






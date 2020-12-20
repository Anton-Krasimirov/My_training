def even_odd(x):
    even = 0
    odd = 0
    for n in range(len(x)):
        i = int(x[n])
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print(f"Odd sum = {odd}, Even sum = {even}")
num = input()

even_odd(num)

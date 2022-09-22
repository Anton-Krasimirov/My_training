'''числата на фибоначи се получават от збора на дадени ни  две числа
 тоест всяко следващо , трето и нататък се получава от збора на предходните две '''

def iterate_fib(num):
    fib0 = 0
    fib1 = 1
    result = 0
    all_numbers = [0, 1]
    for _ in range(num - 1):
        result = fib0 + fib1
        all_numbers.append(result)
        fib0, fib1 = fib1, result
    return result, all_numbers


n = int(input())
print(iterate_fib(n))
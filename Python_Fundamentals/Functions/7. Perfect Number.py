def is_perfect(number):
    divisors = 0
    for i in range(1, number):
        if number % i == 0:
            divisors += i
    return divisors == number

number = int(input())
if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

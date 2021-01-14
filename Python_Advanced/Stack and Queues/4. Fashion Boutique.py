def rack_of_shop(stock, count):
    count_rack = 0
    sum_clothes = 0
    while stock:
        value = stock.pop()
        if count >= (sum_clothes + value):
            if len(stock) == 0 and sum_clothes == 0:
                count_rack += 1
                break
            sum_clothes += value
            if len(stock) == 0 and sum_clothes != 0:
                count_rack += 1
        else:
            count_rack += 1
            sum_clothes = 0
            stock.append(value)
    print(count_rack)


rack_of_shop([int(x) for x in input().split()], int(input()))



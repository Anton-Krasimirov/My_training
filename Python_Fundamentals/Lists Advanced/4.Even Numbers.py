numbers = list(map(int, input().split(", ")))
# splitvame vxoda, obxojadme go s map, pri obxoda labdata go intva i go
# slaga v spisak
even = []

for i in range(len(numbers)):# cikala varti po index zaradi len
    if numbers[i] % 2 == 0:# [] kazva da stoinosta v spisaka
        even.append(i)# ()dobavq indexa v lista

print(even)


# numbers = map(int, input().split(", "))
# print([index for index, number in enumerate(numbers) if number % 2 == 0])

# print([i for i, n in enumerate(map(int, input().split(", "))) if n % 2 == 0])
# cqlata zadach v edin red
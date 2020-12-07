elements = input().split()

list_products = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    list_products[key] = int(value)

print(list_products)

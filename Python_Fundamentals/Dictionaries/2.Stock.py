text = input().split()

list_stock = {}

for i in range(0, len(text), 2):
    product = text[i]
    count = text[i + 1]
    list_stock[product] = int(count)
# list_stock = {text[idx]: int(text[idx + 1]) (for inx in range(0, len(text), 2)}
# sazdava rechnika i zamestva for cikala

check = input().split()

for p in check:
    if p in list_stock:
        quantity = list_stock[p]
        print(f"We have {quantity} of {p} left")
    else:
        print(f"Sorry, we don't have {p}")

# from collections import defaultdict
#
# data = input().split()
# elements = defaultdict(int)# moje da e i dr stoinost vmesto int
#
# for i in range(0, len(data), 2):
#     elements[data[i]] = int(data[i + 1])
#
# search_pr = input().split()
# for product in search_pr:
#     quantity = elements[product]# stoinosta na key-savpadasht s product v elements-rechnika
#     if quantity:
#         print(f"We have {quantity} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")

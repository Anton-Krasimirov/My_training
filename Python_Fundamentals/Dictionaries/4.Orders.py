stock_br = {}
stock_price = {}

while True:
    text = input()
    if text == "buy":
        break

    (product, price_str, count_str) = text.split()
    price = float(price_str)
    count = int(count_str)

    stock_price[product] = price

    if product not in stock_br:
        stock_br[product] = count
    else:
        stock_br[product] += count
for key, count in stock_br.items():
    totalprice = count * stock_price[key]

    print(f"{key} -> {totalprice:.2f}")
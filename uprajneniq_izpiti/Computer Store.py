tottal_price = 0

command = input()
while command:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        tottal_price += price

    command = input()
midle_price = tottal_price
only_tax = tottal_price * 0.2
tottal_price *= 1.2


if command == "special":
    tottal_price *= 0.9

if tottal_price <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {midle_price:.2f}$')
    print(f"Taxes: {only_tax:.2f}$")
    print("-----------")
    print(f"Total price: {tottal_price:.2f}$")
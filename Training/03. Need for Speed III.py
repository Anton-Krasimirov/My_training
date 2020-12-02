# n = int(input())
#
# cars = {}
#
# for i in range(n):
#     data = input().split("|")
#     car = data[0]
#     mileage = int(data[1])
#     fuel = int(data[2])
#
#     cars[car] = {}
#     cars[car]["mileage"] = mileage
#     cars[car]["fuel"] = fuel
#
# info = input()
# while info != "Stop":
#     index = info.split(" : ")
#     command = index[0]
#     car = index[1]
#     if command == "Drive":
#         distance = int(index[2])
#         fuel = int(index[3])
#         if cars[car]["fuel"] < fuel:
#             print("Not enough fuel to make that ride")
#         else:
#             cars[car]["mileage"] += distance
#             cars[car]["fuel"] -= fuel
#             print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
#         if cars[car]["mileage"] >= 100000:
#             print(f"Time to sell the {car}!")
#             del cars[car]
#     elif command == "Refuel":
#         fuel = int(index[2])
#         liters = 75 - cars[car]["fuel"]
#         cars[car]["fuel"] += fuel
#         if cars[car]["fuel"] >= 75:
#             cars[car]["fuel"] = 75
#             print(f"{car} refueled with {liters} liters")
#         else:
#             print(f"{car} refueled with {fuel} liters")
#     elif command == "Revert":
#         kilometers = int(index[2])
#         cars[car]["mileage"] -= kilometers
#         if cars[car]["mileage"] >= 10000:
#             print(f"{car} mileage decreased by {kilometers} kilometers")
#         else:
#             cars[car]["mileage"] = 10000
#     info = input()
# sorted_list = sorted(cars.keys(), key=lambda c: (-cars[c]["mileage"], c))
# for car in sorted_list:
#      print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")


n = int(input())

cars = {}

for _ in range(n):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {"mileage": mileage, "fuel": fuel}


data = input()

while not data == "Stop":
    command_data = data.split(' : ')
    command = command_data[0]
    if command == "Drive":
        car = command_data[1]
        distance = int(command_data[2])
        fuel = int(command_data[3])
        if fuel > cars[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command == "Refuel":
        car = command_data[1]
        fuel = int(command_data[2])
        current_fuel = cars[car]['fuel']
        fuel_to_fill = cars[car]['fuel'] + fuel
        if fuel_to_fill > 75:
            print(f"{car} refueled with {75-current_fuel} liters")
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == "Revert":
        car = command_data[1]
        kilometers = int(command_data[2])
        mileage_left = cars[car]['mileage'] - kilometers
        if mileage_left < 10000:
            cars[car]['mileage'] = 10000
        else:
            cars[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    data = input()

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
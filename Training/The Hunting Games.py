days = int(input())
players = int(input())
all_energy = float(input())
water_day_one = float(input())
food_day_one = float(input())
all_water = days * players * water_day_one
all_food = days * players * food_day_one

for day in range(1, days + 1):
    energy = float(input())
    if (all_energy - energy) >= 0:
        all_energy -= energy
        if day % 3 == 0:
            all_food -= (all_food / players)
            all_energy += (all_energy * 0.1)
        if day % 2 == 0:
            all_water -= (all_water * 0.3)
            all_energy += (all_energy * 0.05)
    else:
        print(f"You will run out of energy. You will be left with {all_food:.2f} food and {all_water:.2f} water.")
        exit()

print(f'You are ready for the quest. You will be left with - {all_energy:.2f} energy!')

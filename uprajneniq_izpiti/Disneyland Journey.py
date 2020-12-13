cost_journey = int(input())

months = int(input())
middle_money = 0
for month in range(1, months + 1):
    if month % 4 == 0:
        middle_money *= 1.25
    elif not month == 1 and not month % 2 == 0:
        middle_money -= middle_money * 0.16
    middle_money += (cost_journey * 0.25)

if cost_journey < middle_money:
    print(f"Bravo! You can go to Disneyland and you will have {middle_money - cost_journey:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {cost_journey - middle_money:.2f}lv. more.")
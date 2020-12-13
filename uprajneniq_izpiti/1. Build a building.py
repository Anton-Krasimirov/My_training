budget = float(input())
start_budget = float(input())
inv = int(input())

money = start_budget

for i in range(1, inv + 1):
    give_money = float(input())
    print(f'Investor {i} gave us {give_money:.2f}.')

    money += give_money

    if budget <= money:
        extra_money = money - budget
        print(f'We will manage to build it. Start now! Extra money - {extra_money:.2f}.')
        break

if budget > money:
    less_money = budget - money

    print(f'Project can not start. We need {less_money:.2f} more.')

days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plunders = 0
for day in range(1, days + 1):
    plunders += daily_plunder
    if day % 3 == 0:
        plunders += (daily_plunder * 0.5)
    if day % 5 == 0:
        plunders -= (plunders * 0.3)
if plunders >= expected_plunder:
    print(f"Ahoy! {plunders:.2f} plunder gained.")

else:
    percentage = (plunders * 100) / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")
one = int(input())
two = int(input())
three = int(input())
student = int(input())

count = 0
pause = 0

all_time = one + two + three

while student > all_time:
    student -= all_time
    count += 1
    if count % 3 == 0:
        pause += 1

if student != 0:
    count += 1

print(f'Time needed: {count + pause}h.')

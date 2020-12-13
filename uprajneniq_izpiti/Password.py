import re
n = int(input())

validator = r"(.+)>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$"

for i in range(n):
    pas = input()
    valid_pass = re.fullmatch(validator, pas)
    if valid_pass:
        rgoup_1 = valid_pass[2]
        rgoup_2 = valid_pass[3]
        rgoup_3 = valid_pass[4]
        rgoup_4 = valid_pass[5]
        valid_password = rgoup_1 + rgoup_2 + rgoup_3 + rgoup_4
        print(f'Password: {valid_password}')
    else:
        print("Try another password!")

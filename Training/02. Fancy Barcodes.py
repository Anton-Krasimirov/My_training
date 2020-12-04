import re

n = int(input())

r_code = "(@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+)"

for i in range(n):
    line = input()
    code = re.findall(r_code, line)
    group = ""
    if not len(code) == 0:
        for sim in code[0]:
            if sim.isdigit():
                group += sim
        if group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {group}")
    else:
        print("Invalid barcode")


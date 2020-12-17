
def data_type(type):
    if type == "int":
        return int(count) * 2
    elif type == "real":
        return int(count) * 1.5
    elif type == "string":
        return "$" + (count) + "$"



type = input()
count = input()
print(data_type(type))

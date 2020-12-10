list = input().split()

string = ""

for i in list:
    n = i * len(i)
    string += n
print(string)
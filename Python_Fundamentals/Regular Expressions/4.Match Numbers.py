import re
text = input()
pattern = r"(^|(?<=\s))(-?)\d+([\.\d]+)?($|(?=\s))"# (^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s))
res = re.finditer(pattern, text)
for r in res:
    print(r[0], end=" ")

# import re
# text = input()
# pattern = r"(^|(?<=\s))(-?)\d+([\.\d]+)?($|(?=\s))"# (^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s))
# res = re.finditer(pattern, text)
# res = [n.group(0) for n in res]# nulata moje da ne se izpishe , default-na e
# print(*res)

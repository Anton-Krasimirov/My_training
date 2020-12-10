# text = input()
#
# for i in range(len(text)):
#     ch = text[i]
#     if i + 1 == len(text):
#         print(ch, end="")
#         break
#     if ch != text[i + 1]:
#         print(ch, end="")

text = input()

line = ""
for i in range(len(text)):
    ch = text[i]
    if i + 1 == len(text) or ch != text[i + 1]:
        line += ch


print(line)





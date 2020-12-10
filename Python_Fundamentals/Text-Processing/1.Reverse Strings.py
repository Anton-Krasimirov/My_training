# text = input()
# word = ""
# while text != "end":
#     for i in text[::-1]:
#         word += i
#     print(f'{text} = {word}')
#     word = ""
#     text = input()

text = input()

word = ""

while text != "end":
    for i in reversed(text):
        word += i
    print(f'{text} = {word}')
    word = ""
    text = input()


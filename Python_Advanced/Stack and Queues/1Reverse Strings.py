def reverced_text(text):
    txt = []
    for ch in text:
        txt.append(ch)
    reverced_new_text = []
    while txt:
        ch = txt.pop()
        reverced_new_text.append(ch)
    return "".join(reverced_new_text)
print(reverced_text(input()))

# # кратка версия
# text = input()
# text = text[::-1]
# print(text)

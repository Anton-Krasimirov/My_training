# ban_words = input().split(", ")
# # word1, word2 = ban_words
# #
# # text = input()
# #
# # if word1 in text:
# #     text = text.replace(word1, "*" * len(word1))
# # if word2 in text:
# #     text = text.replace(word2, "*" * len(word2))
# #
# # print(text)

bann_words = input().split(", ")
text = input()

for word in bann_words:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)
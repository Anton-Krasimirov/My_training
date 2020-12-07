text = input().split()

dictionary = {}

for word in text:
    word_low = word.lower()
    if word_low not in dictionary:
        dictionary[word_low] = 0

    dictionary[word_low] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
     print(key, end=" ")

# from collections import defaultdict
#
# words = input().split()
#
# words_count = defaultdict(int)
#
# for word in words:
#     words_count[word.lower()] += 1
#
# print(' '.join([word for word, value in words_count.items() if value % 2 != 0]))
#

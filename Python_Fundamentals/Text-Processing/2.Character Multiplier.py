text = input().split()
first_word = text[0]
second_word = text[1]

tottal_sum = 0
smal_len = min(len(first_word), len(second_word))

for i in range(smal_len):
    result = ord(first_word[i]) * ord(second_word[i])
    tottal_sum += result

bigest_word = first_word
if len(first_word) < len(second_word):
    bigest_word = second_word

for i in range(smal_len, len(bigest_word)):
    tottal_sum += ord(bigest_word[i])


print(tottal_sum)
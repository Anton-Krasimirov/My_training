n = int(input())

synonyms = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    list = ', '.join(synonym)
    print(f'{word} - {list}')


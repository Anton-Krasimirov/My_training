text = input().split(", ")

for word in text:
    if len(word) <= 16 and len(word) >= 3:

        if word.isalnum() or "-" in word or '_' in word:
            print(word)

text = [x for x in input().split()]

data = input()
while not data == "Stop":
    command = data.split()[0]
    if command == "Delete":
        idx = int(data.split()[1])
        if idx in range(len(text)):
            text.pop(idx)
    elif command == "Swap":
        word1 = data.split()[1]
        word2 = data.split()[2]
        if word2 in text and word1 in text:
            idx1 = text.index(word1)
            idx2 = text.index(word2)
            text[idx1] = word2
            text[idx2] = word1
    elif command == "Put":
        idx = int(data.split()[2])
        word = data.split()[1]
        if idx == len(text) - 1:
            text.append(word)
        else:
            text.insert(idx - 1, word)
    elif command == "Sort":
        pass
    elif command == "Replace":
        pass
    data = input()



print(" ".join(text))
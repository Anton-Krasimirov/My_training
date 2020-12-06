def decode(word):
    num = ""
    for ch in word:
        if not str(ch).isdigit():
            break
        num += ch

    ascii = int(num)
    r_num = chr(ascii)
    new_word = word.replace(num, r_num)
    return new_word


def replace_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def decript(word):
    res = decode(word)
    res = replace_word(res)
    return res



message = list(input().split())
new_message = []# [decript(word) for word in message]

for word in message:
    word = decript(word)
    new_message.append(word)

print(" ". join(new_message))

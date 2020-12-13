def take_odd(text):
    new_text = ""
    for i in range(1, len(text), 2):
        new_text += text[i]
    print(new_text)
    return new_text

def cut(text, idx, lenght):
    new_text = text[:idx] + text[idx + lenght:]
    print(new_text)
    return new_text

def substitude_make(text, str1, str2):
    new_text = text.replace(str1, str2)
    print(new_text)
    return new_text

text = input()

info = input()
while not info == "Done":
    data = info.split()
    if data[0] == "TakeOdd":
        text = take_odd(text)
    elif data[0] == "Cut":
        idx = int(data[1])
        lenght = int(data[2])
        text = cut(text, idx, lenght)
    elif data[0] == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in text:
            text = substitude_make(text, substring, substitute)
        else:
            print("Nothing to replace!")
    info = input()
print(f"Your password is: {text}")
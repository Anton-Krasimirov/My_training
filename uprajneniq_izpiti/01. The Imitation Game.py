text = input()

in_comm = input()
while not in_comm == "Decode":
    data = in_comm.split("|")
    command = data[0]
    if command == "Move":
        number = int(data[1])
        sub_text = text[:number]
        text = text[number:] + sub_text
    elif command == "Insert":
        idx = int(data[1])
        if idx in range(len(text) + 1):
            sim = data[2]
            text = text[:idx] + sim + text[idx:]
    elif command == "ChangeAll":
        sub = data[1]
        repl = data[2]
        text = text.replace(sub, repl)
    in_comm = input()
print(f"The decrypted message is: {text}")
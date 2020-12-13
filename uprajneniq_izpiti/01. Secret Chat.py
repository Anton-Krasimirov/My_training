text = input()

message = input()
while message != "Reveal":
    index = message.split(":|:")
    command = index[0]
    if command == "InsertSpace":
        idx = int(index[1])
        text = text[:idx] + " " + text[idx:]
        print(text)
    elif command == "Reverse":
        peace = index[1]
        if peace in text:
            text = text.replace(peace, "", 1)
            text += peace[::-1]
            print(text)
        else:
            print("error")
    elif command == "ChangeAll":
        first_str = index[1]
        last_str = index[2]
        text = text.replace(first_str, last_str, -1)
        print(text)
    message = input()

print(f"You have a new text message: {text}")
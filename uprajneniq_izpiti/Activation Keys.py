text = input()

data = input()
while data != "Generate":
    data = data.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        if substring in text:
            print(f"{text} contains {substring}")
            data = input()
            continue
        else:
            print("Substring not found!")
            data = input()
        continue
    elif command == "Flip":
        stat_idx = int(data[2])
        end_idx = int(data[3])
        if data[1] == "Upper":
            peace_text = text.upper()[stat_idx:end_idx]
            text = text[:stat_idx] + peace_text + text[end_idx:]
            print(text)
            data = input()
        elif data[1] == "Lower":
            peace_text = text.lower()[stat_idx:end_idx]
            text = text[:stat_idx] + peace_text + text[end_idx:]
            print(text)
            data = input()
        continue
    elif command == "Slice":
        stat_idx = int(data[1])
        end_idx = int(data[2])
        text = text[:stat_idx] + text[end_idx:]
        print(text)
        data = input()

print(f"Your activation key is: {text}")


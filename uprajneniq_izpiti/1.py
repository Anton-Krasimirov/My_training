text = input()

in_put = input()
while in_put != "Finish":
    data = in_put.split()
    comm = data[0]
    if comm == "Replace":
        sim1 = data[1]
        sim2 = data[2]
        text = text.replace(sim1, sim2)
        print(text)
    elif comm == "Cut":
        idx1 = int(data[1])
        idx2 = int(data[2])
        if idx1 in range(len(text) + 1) and idx2 in range(len(text) + 1):
            text = text[:idx1] + text[idx2 + 1:]
            print(text)
        else:
            print("Invalid indices!")
    elif comm == "Make":
        sub_comm = data[1]
        if sub_comm == "Upper":
            text = text.upper()
            print(text)
        elif sub_comm == "Lower":
            text = text.lower()
            print(text)
    elif comm == "Check":
        substring = data[1]
        if substring in text:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif comm == "Sum":
        start_idx = int(data[1])
        end_idx = int(data[2])
        ascitext = 0
        if start_idx in range(len(text) + 1) and end_idx in range(len(text) + 1):
            subtext = text[start_idx:end_idx + 1]
            for i in subtext:
                x = ord(i)
                ascitext += x
            print(ascitext)
        else:
            print("Invalid indices!")
    in_put = input()

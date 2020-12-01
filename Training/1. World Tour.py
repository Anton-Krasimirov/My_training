text = input()

while True:
    data = input()
    if data == "Travel":
        print(f"Ready for world tour! Planned stops: {text}")
        break
    idx = data.split(":")
    comm = idx[0]
    if comm == "Add Stop":
        index = int(idx[1])
        string = idx[2]
        if index != ":" or index != "-" or string.isalpha():
            set1 = text[:index]
            set2 = text[index:]
            text = set1 + string + set2
            print(text)
    elif comm == "Remove Stop":
        start_index = int(idx[1])
        end_index = int(idx[2])
        if start_index != ":" or end_index != "-":
            text = text[:start_index] + text[end_index + 1:]
            print(text)
    elif comm == "Switch":
        old_string = idx[1]
        new_string = idx[2]
        if old_string in text:
            text = text.replace(old_string, new_string)
            print(text)




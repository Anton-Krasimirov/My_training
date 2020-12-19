def get_char_in_range(first, second):
    result = []
    start = ord(min([first, second]))
    end = ord(max([first, second]))
    for i in range(start + 1, end):
        character = chr(i)
        result.append(character)
    return result

first_char = input()
second_char = input()


total_result = get_char_in_range(first_char, second_char)
print(" ".join(total_result))




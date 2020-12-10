def alphabet_position(alpha):
    position = ord(alpha) - 64
    if alpha.islower():
        position = ord(alpha) - 96
    return position


def calculate_word(word):
    first_alpha = word[0]
    second_alpha = word[-1]
    num = int(word[1:-1])
    total_sum = 0

    if first_alpha.isupper():
        total_sum = num / alphabet_position(first_alpha)
    else:
        total_sum = num * alphabet_position(first_alpha)
    if second_alpha.isupper():
        total_sum = total_sum - alphabet_position(second_alpha)
    else:
        total_sum = total_sum + alphabet_position(second_alpha)

    return total_sum


words = input().split()
result = 0
for word in words:
    mid = calculate_word(word)
    result += mid
print(f"{result:.2f}")

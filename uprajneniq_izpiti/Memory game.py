def play_round(cards, i_1, i_2, round_num):
    if i_1 == i_2 or i_1 not in range(len(cards)) or i_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{round_num}a"
        middle = len(cards) // 2
        cards.insert(middle, card)
        cards.insert(middle + 1, card)
        return cards

    if cards[i_1] == cards[i_2]:
        element = cards[i_1]
        print(f"Congrats! You have found matching elements - {element}!")
        cards.remove(element)
        cards.remove(element)
        return cards
    print("Try again!")
    return cards


memory_cards = input().split()
command = input()

counter = 0

while not command == 'end':
    index_1, index_2 = [int(el) for el in command.split()]
    counter += 1
    memory_cards = play_round(memory_cards, index_1, index_2, counter)
    if len(memory_cards) == 0:
        print(f"You have won in {counter} turns!")
        exit(0)
    command = input()

print("Sorry you lose :(")
print(' '.join(memory_cards))

# data = list(input().split())
#
# count = 0
#
# cards = input()
# while not cards == "end":
#     count += 1
#     idx1 = int(cards.split()[0])
#     idx2 = int(cards.split()[1])
#
#     card1 = data[idx1]
#     card2 = data[idx2]
#     if idx1 == idx2 or idx1 not in range(len(data) or idx2 not in range(len(data))):
#         mid_index = len(data) // 2
#         data.insert(mid_index, f"-{count}a")
#         data.insert(mid_index, f"-{count}a")
#         print("Invalid input! Adding additional elements to the board")
#         cards = input()
#         continue
#     elif card1 != card2:
#         print("Try again!")
#         cards = input()
#         continue
#     else:
#         data.remove(card1)
#         data.remove(card2)
#         print(f"Congrats! You have found matching elements - {card1}!")
#         if not data:
#             print(f"You have won in {count} turns!")
#             exit()
#     cards = input()
#
# print("Sorry you lose :(")
# print(" ".join(data))

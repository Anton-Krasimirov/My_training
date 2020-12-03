list_of_num = list(map(int, input().split(", ")))

num_grups = max(list_of_num) // 10# num_grups = math.ceil(max(list_of_num) / 10)
if max(list_of_num) % 10 != 0:
    num_grups += 1

for i in range(1, num_grups + 1):
    up = i * 10
    low = up - 10
    nums = [num for num in list_of_num if low < num <= up]

    print(f"Group of {i * 10}'s: {nums}")
    nums = []


# list_of_num = list(map(int, input().split(", ")))
#
# num_grups = max(list_of_num) // 10
# if max(list_of_num) % 10 != 0:
#     num_grups += 1
#
# for i in range(1, num_grups + 1):
#     nums = []
#     for num in list_of_num:
#         up = i * 10
#         low = up - 10
#         if low < num <= up:
#             nums.append(num)
#     print(f"Group of {i * 10}'s: {nums}")
#     nums = []




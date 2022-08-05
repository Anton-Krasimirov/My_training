nums = [int(x) for x in input().split()]

for i in range(1, len(nums)):
    for j in range(i, 0, -1): # за да обходим назад от където сме , от i назад до индекс 0
        if nums[j] < nums[j - 1]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]

        else:
            break #  с цел по малко итерации ако първите няколко са подадени начално подредени
print(*nums, sep=' ')
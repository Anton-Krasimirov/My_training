'''Разменяме местата на двойки като ги сравняваме , така при един обход се намира най-голямото и се слага на края'''

nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0# чрез каунтъра спираме цикъла
while not is_sorted:
    is_sorted = True# променяме стойноста , ако не влезе в иф проверката значи е сортиран
    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False# стигне ли до тук списъка не е сортиран
    counter += 1


print(*nums, sep=' ')
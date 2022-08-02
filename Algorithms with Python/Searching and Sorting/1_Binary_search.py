def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r: # когато индексите се разминат сме обходили всичко и нямаме открит резултат
        mid_idx = (l + r) // 2 # задаване на средния индекс (средата)
        mid_element = nums[mid_idx]

        if mid_element == target:
            return mid_idx
        elif target > mid_element:
            l = mid_idx + 1 # местим началния индекс една позиция след средата
        else:
            r = mid_idx - 1 # местим последния индекс една позиция преди средата


    return -1 # по условие да върне -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
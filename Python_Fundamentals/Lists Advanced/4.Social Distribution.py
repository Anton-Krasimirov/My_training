list_populations = list(map(int, input().split(", ")))
count = int(input())

for i in range(1, len(list_populations)):
    min_num = min(list_populations)
    max_num = max(list_populations)
    index = count - min_num
    if index == 0:
        break
    list_populations.remove(max_num)
    list_populations.remove(min_num)
    min_num += index
    max_num -= index
    list_populations.insert(0, min_num)
    list_populations.extend([max_num])

if list_populations[-1] < count:
    print("No equal distribution possible")
else:
    print(list_populations)
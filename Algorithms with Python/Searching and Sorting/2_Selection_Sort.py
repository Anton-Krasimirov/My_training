nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    min_number = nums[idx]# взимаме първото число от масива, в долния фор го сравняваме със всяко следващо
    min_idx = idx
    for next_idx in range(idx + 1, len(nums)):# тук намираме най-малкото, като всяко по-малко го поставяме 1-во и сравняваме с него
        next_number = nums[next_idx]# взимаме следващото число
        if next_number < min_number:
            min_number = next_number
            min_idx = next_idx# min_idx взима индекса на числото кото приема min_number за да се сменят в горния фор цикъл
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx] # тук вече променяме местата в самия масив , горе се сменят само в променливите


print(*nums, sep=' ')
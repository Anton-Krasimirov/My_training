def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:# ако на левия списък първата стойност не е по малка , слиза долу и взима директно от десния първа ст.
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]# тук знаем че масива е бил вече сортиран или е от 1 елемент и взимаме най лявата позиция  на десния масив
            right_idx += 1
        result_idx += 1# което от двете да е извършено променяме индекса за да се движим в новосъздаващия се масив
    '''това се прави за да не останат недобавени позиции в някои масив заради сортирането, ако вземем позиците само от един масив ,
    първия цикъл ще спре итерациите и ще останат недобавени позиции'''
    while left_idx < len(left):#
            result[result_idx] = left[left_idx]
            left_idx += 1
            result_idx += 1

    while right_idx < len(right):# това се прави по сищата причина като горния цикъл но за десен масив, ако е десен няма да влезе в горни цикъл и обратно
            result[result_idx] = right[right_idx]
            right_idx += 1
            result_idx += 1

    return result

def murge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]
    '''до тук разделяме масива на две , долу го подаваме в нова функция която рекурсивно ще го разделя до масиви от по 1 символ'''
    return merge_arrays(murge_sort(left), murge_sort(right))
    '''в тази функция рецурсивните извиквания ще се извършват последователно, първо лявята част , докато не стигне 1
    после дясната част, ще започнат да се изпращат по обратен ред '''


nums = [int(x) for x in input().split()]

result = murge_sort(nums)

print(*result, sep=' ')
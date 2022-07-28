def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):# при всяко извикжане долу нум е 1, idx се променя със (idx + 1)
        arr[idx] = num
        nested_loops(idx + 1, arr)# рецурсията се враща до предната итерация , когато е приключила


n = int(input())
arr = [None] * n

nested_loops(0, arr)
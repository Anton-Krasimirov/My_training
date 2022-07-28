def count_all_paths(row, col, rows, cols):
    if row >= rows or col >= cols:# проверка дали сме в рамката на матрицата
        return 0
    if row == rows - 1 and col == cols - 1:# проверка дали съм на изхода
        return 1

    result = 0
    result += count_all_paths(row, col + 1, rows, cols)
    '''движение само на дясно , излезе ли от рамката връща до последното и слиза на 
    долната рецурсивна функция'''
    result += count_all_paths(row + 1, col, rows, cols)
    '''движението е само на долу , ако излезе , sсе връща едно на зад и предава на горната функция'''
    return result


rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))
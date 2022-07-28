'''генерира всички възможни комбинации със 1/0 за n брой стйности '''

def generate(idx, vector):
    if idx >= len(vector):
        print(*vector,  sep='')#принтирай текущите числа разделени по нищо
        return
    for num in range(2):
        vector[idx] = num
        generate(idx + 1, vector)


n = int(input())
vector = [0] * n # създавам речник от нули с дължина n

generate(0, vector)

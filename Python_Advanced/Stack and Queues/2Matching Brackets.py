def sub_expretions(text):
    s = []
    result = []

    for index in range(len(text)):
        ch = text[index]
        if ch == '(':
            s.append(index)# взимам индекса на първата скоба
        elif ch == ')':
            start_index = s.pop()# взимам индекса на последно добавената скоба, първата си остава в листа
            result.append(text[start_index:index + 1])
    return result


for expr in sub_expretions(input()):
    print(expr)
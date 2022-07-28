def find_all_paths(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):# проверяваме дали е потенциално решение ,елиминира се невалидни стойности
        return

    if lab[row][col] == '*':
        return

    if lab[row][col] == 'v':
        return

    path.append(direction)  # съхраняваме пътя по който съм минал, преди проверката за е , за да отпечата целия път
    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'# маркираме от къде съм минал

        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        find_all_paths(row, col + 1, lab, 'R', path)

        lab[row][col] = '-'# отмаркирам клетката , за да може следващото решение да я ползва отново
    path.pop()# изчистваме пътя



rows = int(input())
cols = int(input())


lab = []
for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, '', [])
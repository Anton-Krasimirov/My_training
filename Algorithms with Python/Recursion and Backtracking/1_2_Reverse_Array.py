def reverse_sumbols(idx, sumbols):
    if idx == len(sumbols) // 2:
        return
    swap_idx = len(sumbols) - 1 - idx
    sumbols[idx], sumbols[swap_idx] = sumbols[swap_idx], sumbols[idx]
    reverse_sumbols(idx + 1, sumbols)
    '''може без return sumbols , ще се обработи simbols получен от входа'''


sumbols = input().split()

reverse_sumbols(0, sumbols)

print(' '.join(sumbols))
# ==========================================
'''без рекурсия би следвало да е по тоззи начин'''
res = reversed(sumbols)
print(*res, sep=' ')
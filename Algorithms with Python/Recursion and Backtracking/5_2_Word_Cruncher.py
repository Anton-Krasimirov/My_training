'''кои думи можем да съчетаем за да получим таргет думата'''
def find_all_solutions(idx, target, words_by_idx, word_count, used_words):
    if idx >= len(target):# така разбираме че сме попълнили таргета
        print(' '.join(used_words))
        return
    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if word_count[word] == 0:# дали я имаме тази дума
            continue
        used_words.append(word)# казвам че съм използвал думата
        word_count[word] -= 1# колко пъти е намерена думата за да се знае колко пъти може да се ползва

        find_all_solutions(idx + len(word), target, words_by_idx, word_count, used_words)

        used_words.pop()# махам ако не съм намерил други решения
        word_count[word] += 1# тук вече не ползваме думата

words = input().split(", ")
target = input()

'''предварително проверка на кой индекс коя и колко думи може да се сложат'''
words_by_idx = {}
word_count = {}# колко пъти може да ползвам дадена дума
for word in words:
    if word in word_count:
        word_count[word] += 1
        continue# ако имаме дума пасваща в повече в условието(повтряща но не нужна) , да не я добавя и нея
    word_count[word] = 1

    '''тирсене на индехите на дума и дали я има , чрез олавяне на грешка'''
    try:#.index почва да търси винаги от индех 0 , освен ако не му посочим изрично от къде
        idx = 0
        while True:
            idx = target.index(word, idx)# индекса от които да търсим на дясно .index(_____, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []# инициализираме масива в които да поставим всички думи които можем на този индекс
            words_by_idx[idx].append(word)
            idx += len(word)# променяме индекса да търси след думата вече
    except ValueError:# стигаме до тук защото или стринга ще свърши или няма да намерим повече пъти думата
        pass


find_all_solutions(0, target, words_by_idx, word_count, [])
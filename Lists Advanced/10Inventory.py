def collect(l, w):
    if w not in l:
        l.append(w)
    return l


def drop(l, w):
    if w in l:
        l.remove(w)
    return l


def combine_items(l, w):
    old_item = w.split(":")[0]
    new_item = w.split(":")[1]
    if old_item in l:
        for i in range(len(l)):
            if old_item == l[i]:
                l.insert(i + 1, new_item)
    return l

def renew(l, w):
    if w in l:
        for i in l:
            if i == w:
                l.remove(w)
                l.append(i)
    return l

journal = input().split(", ")

data = input()
while not data == "Craft!":
    command = data.split(" - ")[0]
    word = data.split(" - ")[1]
    if command == "Collect":
        collect(journal, word)
    elif command == "Drop":
        drop(journal, word)
    elif command == "Combine Items":
        combine_items(journal, word)
    elif command == "Renew":
        renew(journal, word)

    data = input()
print(", ".join(journal))


# items = input().split(", ")
#
# data = input()
#
#
# def is_item_in_list(items_list, i):
#     if i in items_list:
#         return True
#     return False
#
#
# def collect_item(items_list, i):
#     if not is_item_in_list(items_list, i):
#         items_list.append(i)
#     return items_list
#
#
# def drop_item(items_list, i):
#     if is_item_in_list(items_list, i):
#         items_list.remove(i)
#     return items_list
#
#
# def combine_items(items_list, i):
#     old_item = i.split(":")[0]
#     new_item = i.split(":")[1]
#     if is_item_in_list(items_list, old_item):
#         index_old_item = items_list.index(old_item)
#         index_new_item = index_old_item + 1
#         items_list.insert(index_new_item, new_item)
#     return items_list
#
#
# def renew_item(items_list, i):
#     if is_item_in_list(items_list, i):
#         items_list.remove(i)
#         items_list.append(i)
#     return items_list
#
#
# while not data == "Craft!":
#     command, item = data.split(" - ")
#
#     if command == "Collect":
#         items = collect_item(items, item)
#     elif command == "Drop":
#         items = drop_item(items, item)
#     elif command == "Combine Items":
#         items = combine_items(items, item)
#     elif command == "Renew":
#         items = renew_item(items, item)
#
#     data = input()
#
# print(", ".join(items))
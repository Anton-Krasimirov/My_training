shelf_books = input().split("&")

data = input()

while not data == "Done":
    command = data.split(" | ")[0]
    book_name = data.split(" | ")[1]
    if command == "Add Book":
        if not book_name in shelf_books:
            shelf_books.insert(0, book_name)
    elif command == "Take Book":
        if book_name in shelf_books:
            shelf_books.remove(book_name)
    elif command == "Swap Books":
        book_name2 = data.split(" | ")[2]
        if book_name in shelf_books and book_name2 in shelf_books:
            idx2 = shelf_books.index(book_name2)
            idx1 = shelf_books.index(book_name)
            shelf_books.remove(book_name2)
            shelf_books.insert(idx2, book_name)
            shelf_books.remove(book_name)
            shelf_books.insert(idx1, book_name2)
    elif command == "Insert Book":
        shelf_books.append(book_name)
    elif command == "Check Book":
        index = int(book_name)
        if index in range(len(shelf_books)):
            print(shelf_books[index])
    data = input()

print(", ".join(shelf_books))
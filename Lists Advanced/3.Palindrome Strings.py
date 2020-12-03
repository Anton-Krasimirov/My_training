# def is_palindrome(word):
#     return word == word[::-1]
# return word == "".join(reversed(word)  ispalnqva sashtototo


words = input().split()
serched = input()
palindroms = []

for word in words:
    if word == "".join(reversed(word)):
        palindroms.append(word)
    # palindroms = [word for word in words if is_palindrome(word)]

print(palindroms)
print(f"Found palindrome {words.count(serched)} times")


# def is_palindrome(word):
#     return word == word[::-1]
#
# words = input().split()
# serched = input()
#
# palindroms = [word for word in words if is_palindrome(word)]
# print(palindroms)
# print(f"Found palindrome {words.count(serched)} times")


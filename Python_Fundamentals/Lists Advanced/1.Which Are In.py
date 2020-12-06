list1 = input().split(", ")
text = input()  # ostavqme go strin za da tirsim v celiq str samo chast ot lst1

new = []# new = [word for word in list1 if word in text]

for word in list1:
    if word in text:
        new.append(word)

print(new)




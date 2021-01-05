x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x  # tozi red  e dobaven
        x = "nonlocal"
        print("inner:", x)


    def change_global():
        global x   # tozi red e dobaven
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

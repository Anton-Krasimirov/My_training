n = int(input())

pieses = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieses[piece] = {"composer": composer, "key": key}

in_put = input()
while not in_put == "Stop":
    comm = in_put.split("|")[0]
    piece = in_put.split("|")[1]
    if comm == "Add":
        composer = in_put.split("|")[2]
        key = in_put.split("|")[3]
        if piece in pieses:
            print(f"{piece} is already in the collection!")
        else:
            pieses[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif comm == "Remove":
        if piece in pieses:
            pieses.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif comm == "ChangeKey":
        new_key = in_put.split("|")[2]
        if not piece in pieses:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieses[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    in_put = input()

sorted_pieses = sorted(pieses.items() ,key=lambda x: (x[0], x[1]["composer"]))
for k, v in sorted_pieses:
    print(f"{k} -> Composer: {v['composer']}, Key: {v['key']}")




rooms = input().split("|")
bitcoins = 0
health = 100
num_room = 0

for room in rooms:
    index = room.split(" ")
    command = index[0]
    count = int(index[1])
    if command == "potion":
        num_room += 1
        if health == 100:
            print(f"You healed for 0 hp.")
            print(f"Current health: 100 hp.")
        elif health + count > 100:
            refil_health = 100 - health
            health = 100
            print(f"You healed for {refil_health} hp.")
            print(f"Current health: {health} hp.")
        elif health + count < 100:
            health += count
            print(f"You healed for {count} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        num_room += 1
        bitcoins += count
        print(f"You found {count} bitcoins.")
    else:
        num_room += 1
        if health <= count:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {num_room}")
            health = 0
            break
        else:
            health -= count
            print(f"You slayed {command}.")


if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
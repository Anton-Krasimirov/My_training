followers = {}

while True:
    data = input()
    if data == "Log out":
        print(f"{len(followers)} followers")
        sorted_followers = dict(sorted(followers.items(), key=lambda x: (-x[1][0], x[0])))
        for key, value in sorted_followers.items():
            print(f"{key}: {sum(value)}")

        break

    command = data.split(": ")
    task = command[0]
    username = command[1]

    if task == "New follower":

        if username in followers:
            continue

        followers[username] = [0, 0]

    elif task == "Like":
        count = int(command[2])

        if username in followers:
            followers[username][0] += count
            continue

        followers[username] = [count, 0]

    elif task == "Comment":

        if username in followers:
            followers[username][1] += 1
            continue

        followers[username] = [0, 1]

    elif task == "Blocked":

        if username in followers:
            followers.pop(username)
            continue

        print(f"{username} doesn't exist.")

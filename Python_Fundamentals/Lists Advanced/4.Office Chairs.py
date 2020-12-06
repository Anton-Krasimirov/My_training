# n = int(input())
#
# plase_less = 0
# free_plase = []
#
# for i in range(1, n + 1):
#
#     room = input().split()
#     plase = len(room[0]) - int(room[1])
#     if plase >= 0:
#         free_plase.append(plase)
#     else:
#         plase_less += 1
#         print(f"{abs(plase)} more chairs needed in room {i}")
#
# if plase_less == 0:
#     print(f"Game on, {sum(free_plase)} free chairs left")

n = int(input())

plase_less = True
free_plase = 0

for i in range(1, n + 1):

    room = input().split()
    plase = len(room[0]) - int(room[1])
    if plase >= 0:
        free_plase += plase
    else:
        plase_less = False
        print(f"{int(room[1]) - len(room[0])} more chairs needed in room {i}")

if plase_less:
    print(f"Game on, {free_plase} free chairs left")
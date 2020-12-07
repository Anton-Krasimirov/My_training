data_bace = {}

string = input()

while string != 'Lumpawaroo':
    if "|" in string:
        args = string.split(" | ")
        side = args[0]
        name = args[1]
        if side not in data_bace:
            data_bace[side] = []
        all_value = []

        for curent_list in data_bace.values():
            all_value += curent_list

        if name not in all_value:
            data_bace[side].append(name)

    else:
        args = string.split(" -> ")
        name = args[0]
        side = args[1]
        old_side = ""
        for key, value in data_bace.items():
            if name in value:# ako imeto go ima kato stoinost
                old_side = key# vzimame imeto na key-a v promenliva
                break

        if old_side != "":# ako sme vzeli imeto na key-a znachi promenqme....
            data_bace[old_side].remove(name)# maxame go it segashniq key
            if side not in data_bace:
                data_bace[side] = []# ako noviq key go nqma go sazdavame
            data_bace[side].append(name)# dobvqme stoinosta v novosazdadeniq key


        else:# ako umeto ne e v nikoi ot keys
            if side not in data_bace:
                data_bace[side] = []
            data_bace[side].append(name)
        print(f"{name} joins the {side} side!")
    string = input()

data_bace = dict(sorted(data_bace.items(), key=lambda x: (-len(x[1]), x[0])))

for side, name in data_bace.items():
    if len(name) == 0:
        continue

    print(f"Side: {side}, Members: {len(name)}")
    for n in sorted(name):
        print(f"! {n}")

# def add_user(forces_dict, side_to_join, user_to_add):
#     for side, users in forces_dict.items():
#         if user_to_add in users:
#             return forces_dict
#     if side_to_join not in forces_dict:
#         forces_dict[side_to_join] = []
#         forces_dict[side_to_join].append(user_to_add)
#     else:
#         if user_to_add not in forces_dict[side_to_join]:
#             forces_dict[side_to_join].append(user_to_add)
#     return forces_dict
#
#
# def transfer_user(forces_dict, side_to_transfer, user_to_transfer):
#     for side, users in forces_dict.items():
#         if user_to_transfer in users:
#             forces_dict[side].remove(user_to_transfer)
#             return add_user(forces_dict, side_to_transfer, user_to_transfer)
#     return add_user(forces_dict, side_to_transfer, user_to_transfer)
#
#
# data = input()
#
# forces = {}
#
# while not data == "Lumpawaroo":
#     data_list = data.split(' | ')
#
#     if len(data_list) > 1:
#         side, user = data.split(' | ')
#         forces = add_user(forces, side, user)
#     else:
#         user, side = data.split(' -> ')
#         forces = transfer_user(forces, side, user)
#         print(f"{user} joins the {side} side!")
#     data = input()
#
#
# ordered_forces = sorted(forces.items(), key=lambda x: (-len(x[1]), x[0]))
#
# for side, users in ordered_forces:
#     if len(users) > 0:
#         print(f"Side: {side}, Members: {len(users)}")
#         for user in sorted(users):
#             print(f"! {user}")

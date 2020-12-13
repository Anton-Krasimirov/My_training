def check_for_duel(dict, name1, name2, dict2):
    player1 = dict[name1].keys()
    player2 = dict[name2].keys()
    for x in player1:
        for y in player2:
            if x == y:
                if int(dict[name1][x]) > int(dict[name2][y]):
                    dict.pop(name2)
                    dict2.pop(name2)
                    break
                else:
                    dict.pop(name1)
                    dict2.pop(name1)
                    break
    return dict, dict2


name_totall_skill = {}
name_pos_skills = {}
in_data = input()
while not in_data == "Season end":
    if not "vs" in in_data:
        player, poss, skill = in_data.split(" -> ")
        skill = int(skill)
        if player in name_pos_skills:
            if not poss in name_pos_skills[player].values():
                name_pos_skills[player][poss] = skill
                name_totall_skill[player] += skill
        else:
            name_pos_skills[player] = {poss: skill}
            name_totall_skill[player] = skill
        in_data = input()
    else:
        player1, player2 = in_data.split(" vs ")
        if player1 in name_pos_skills.keys() and player2 in name_pos_skills.keys():
            name_pos_skills, name_totall_skill = check_for_duel(name_pos_skills, player1, player2, name_totall_skill)
        in_data = input()


name_totall_skill = dict(sorted(name_totall_skill.items(), key=lambda x: (-x[1], x[0])))

kei = [k for k in name_pos_skills.keys()]
value = [v for v in name_pos_skills.values()]
value = [dict(sorted(x.items(), key=lambda kv: (-kv[1], kv[0]))) for x in value]
name_pos_skills = dict(zip(kei, value))

# key = [x for x, v in name_totall_skill.items() if v == max(name_totall_skill.values())]
# print(f"{''.join(key)}: {max(name_totall_skill.values())} skill")
for k, v in name_totall_skill.items():
    print(f"{k}: {v} skill")
    for x, y in name_pos_skills[k].items():
        print(f"- {x} <::> {y}")

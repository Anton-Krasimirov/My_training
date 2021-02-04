from DEFINING_CLASSES_Exercises.guild_system.project.guild import Guild

class Player:
    def __init__(self, name, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self. mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"


    def add_skill(self, skill_name, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):
        to_print = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for k, v in self.skills.items():
            to_print += f"==={k} - {v}\n"
        return to_print


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())



class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name):
        if player_name not in [p.name for p in self.players]:
            return f"Player {player_name} is not in the guild."
        for_remove = [x for x in self.players if x.name == player_name][0]
        self.players.remove(for_remove)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for p in self.players:
            data += p.player_info()
        return data




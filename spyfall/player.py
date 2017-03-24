# object to keep track of players in the game
class player:
    def __init__ (self, discord_user_name, spyfall_role):
        self.name = discord_user_name
        self.role = None

# object to keep track of players in the game
class Player:
    def __init__(self, discord_user_name):
        self.name = discord_user_name
        self.role = None

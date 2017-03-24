# object to keep track of game state
class game:
    def __init__ (self):

        # list of player objects
        self.players = []

        # keeps track of the current location
        self.location = None

    def end_game (self):
        for player in self.players:
            if (player.role == "spy"):
                print("The spy was %s!" % player.discord_user_name)

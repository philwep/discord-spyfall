from player import Player
from random import randint

# object to keep track of game state
class Game:
    def __init__ (self):

        # list of player objects
        self.players = []

        # keeps track of the current location
        self.location = None

    def end_game (self):
        for player in self.players:
            if (player.role == "spy"):
                print("The spy was %s!" % player.discord_user_name)

    def join_player (self, discord_user_name):
        player = Player(discord_user_name)
        self.players.append(player)

    def _assign_roles (self, roles):
        spy = randint(0,len(self.players)-1)
        self.players[spy].role = "spy"

        cur_role = 0
        for player in self.players:
            if (player.role != "spy"):
                player.role = roles[cur_role]

            if (cur_role + 1 >= len(roles)):
                cur_role = 0
            else:
                cur_role += 1


    def start_game (self):
        self._assign_roles()

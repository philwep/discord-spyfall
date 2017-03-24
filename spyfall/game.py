from player import Player
from random import randint
import os
import json

# object to keep track of game state
class Game:
    def __init__(self):

        # list of player objects
        self.players = []

        # keeps track of the current location
        self.location = None

        # locations and roles
        self.locations_file = []

    def end_game(self):
        for player in self.players:
            if (player.role == "spy"):
                print("The spy was %s!" % player.discord_user_name)

    def join_player(self, discord_user_name):
        player = Player(discord_user_name)
        self.players.append(player)

    def leave_player(self, discord_user_name):
        player = Player(discord_user_name)
        if player in self.players:
            self.players.remove(player)

    def assign_roles(self, roles):
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

    def get_locations(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as locations_file:
                self.locations_file = json.load(locations_file)
        else:
            print("The file %s does not exist or cannot be opened" % file_name)

    def get_roles(self, cur_location):
        roles = self.locations_file[cur_location]
        return roles

        # for roles i


    def start_game(self):
        self.assign_roles()

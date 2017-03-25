from player import Player
from random import randint
import sys
import os
import json

# object to keep track of game state
class Game:

    # global variable for config location
    LOCATIONS_FILE = 'spyfall_locations.json'

    def __init__(self):

        # list of player objects
        self.players = []

        # keeps track of the current location (int index of locations json key)
        self.location = None

        # locations, roles and other json settings
        self._game_data = None

    # reveal identity of the spy
    def end_game(self):
        for player in self.players:
            if (player.role == "spy"):
                print("The spy was %s!" % player.discord_user_name)

    # add player to game
    def join_player(self, discord_user_name):
        player = Player(discord_user_name)
        self.players.append(player)

    # remove player from game
    def leave_player(self, discord_user_name):
        player = Player(discord_user_name)
        if player in self.players:
            self.players.remove(player)

    # choose a random location
    def assign_location(self):
        if (self._game_data != None):
            locations = self._game_data['locations']
            self.location = randint(0,len(locations)-1)
        else:
            self._load_data()
            self.assign_location()

    # assign random roles to each player
    def assign_roles(self):
        if (self.location != None):
            spy = randint(0,len(self.players)-1)
            self.players[spy].role = "Spy"

            roles = self._game_data['locations'][self.location]['Roles']
            cur_role = 0
            for player in self.players:
                if (player.role != "Spy"):
                    player.role = roles[cur_role]
                    if (cur_role >= len(roles)-1):
                        cur_role += 1
                    else:
                        cur_role = 0
        else:
            self.assign_location()
            self.assign_roles()

    # update the _game_data variable with contents of LOCATIONS_FILE
    def _load_data(self):
        if os.path.exists(LOCATIONS_FILE):
            with open(LOCATIONS_FILE, 'r') as locations_file:
                self._game_data = json.load(locations_file)
            locations_file.close()

            for location in self.locations_file:
                self.location_names.append(location)
        else:
            print("The file %s does not exist or cannot be opened" % LOCATIONS_FILE)
            sys.exit(-1)

    def start_game(self):
        self._load_data()
        self.assign_location()
        self.assign_roles()

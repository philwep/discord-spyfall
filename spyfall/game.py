from player import Player
import random
import sys
import os
import json

# object to keep track of game state
class Game:

    def __init__(self):

        # variable for config location
        self.LOCATIONS_FILE = 'spyfall_locations.json'


        # list of player objects
        self.players = []

        # keeps track of the current location (int index of locations json key)
        self.location = None

        # locations, roles and other json settings
        self._game_data = None

        # location list
        self.loc_list = []

    # reveal identity of the spy
    def end_game(self):
        for player in self.players:
            if (player.role == "spy"):
                print("The spy was %s!" % player.discord_user_name)

    # add player to game
    def join_player(self, discord_user_name):
        player_exists = False
        for player in self.players:
            if player.name == discord_user_name:
                player_exists = True

        if player_exists:
            print ("That player is already in the game!")
            # Make this send the message so the people can see it
        else:
            player = Player(discord_user_name)
            self.players.append(player)

    # remove player from game
    def leave_player(self, discord_user_name):
        for i in range(len(self.players)-1):
            if self.players[i].name ==  discord_user_name:
                del self.players[i]

    # choose a random location
    def assign_location(self):
        if (self._game_data != None):
            locations = self._game_data['locations']
            self.location = random.randint(0,len(locations)-1)
        else:
            self._load_data()
            self.assign_location()

    # assign random roles to each player
    def assign_roles(self):
        if (self.location != None):
            spy = random.randint(0,len(self.players)-1)
            self.players[spy].role = "Spy"

            roles = self._game_data['locations'][self.location]['Roles']
            for i in range(random.randint(0,10)):
                random.shuffle(roles)
            cur_role = 0
            for player in self.players:
                if (player.role != "Spy"):
                    player.role = roles[cur_role]
                    if (cur_role <= len(roles)-1):
                        cur_role += 1
                    else:
                        cur_role = 0
        else:
            self.assign_location()
            self.assign_roles()

    # removes any pre-existing roles that has been asigned, if exists
    def clear_roles(self):
        for player in self.players:
            player.role = None

    def get_locations(self):
        del self.loc_list[:]
        for i in range(len(self._game_data['locations'])):
            self.loc_list.append(self._game_data['locations'][i]['Location'])

    def purge(self):
        del self.players[:]

    # update the _game_data variable with contents of LOCATIONS_FILE
    def _load_data(self):
        if os.path.exists(self.LOCATIONS_FILE):
            with open(self.LOCATIONS_FILE, 'r') as locations_file:
                self._game_data = json.load(locations_file)
            locations_file.close()
        else:
            print("The file %s does not exist or cannot be opened" % LOCATIONS_FILE)
            sys.exit(-1)

    def start_game(self):
        if (len(self.players) > 0):
            self._load_data()
            self.get_locations()
            self.clear_roles()
            self.assign_location()
            self.assign_roles()
        else:
            print("Must add players first")
            # REPLACE THIS TO SEND A DISCORD MESSAGE INSTEAD

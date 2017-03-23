""" March 09, 2017
@author: Phillip Le
@author: Fabio Colacio
"""

import discord
import asyncio
import random
import os

from player import player
from game import game

def get_data(spyfall_filename):
    '''
    Parses a .csv file

    Args:
        spyfall_filename: .csv file to be opened and parsed into a dictionary that has keys as location names and values as a list that contains all the roles

    Returns:
        A list that has a dictionary pointing to a list

        Example Output:

            [location_name:[role_1, role_2, role_3]]
    '''
    if os.path.exists(spyfall_filename):
        with open(spyfall_filename, 'r') as data_file:
            lines = data_file.readlines()  # read all lines from the file into a list
            roles = {}
            for i in range(len(lines)):
                parts = lines[i].split(',')
                roles[parts[0]] = [point.strip('\n') for point in parts[1:]]
            spyfall_data = roles
            return spyfall_data
    else:
        print("The file %s does not exist or cannot be opened" % spyfall_filename)


def get_current_roles(spyfall_data, current_location):

    current_roles = []
    for role in spyfall_data[current_location]:
        current_roles.append(role)

    for shuffle_times in range(0,random.randint(0,10)):
        random.shuffle(current_roles)

    return current_roles

def main():
    spyfall_data = get_data('spyfall_data.csv')

    locations = []
    for location in spyfall_data:
        locations.append(location)

    players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6']

    current_location = locations[random.randint(0,len(locations) - 1)]

    current_roles = get_current_roles(spyfall_data, current_location)

    print(locations)
    print()
    print(current_location)
    print()
    print(current_roles)

main()

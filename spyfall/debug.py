from game import Game

game = Game()

def start():
    game.start_game()
    print("Location: %s" % game._game_data['locations'][game.location]['Location'])
    print("Roles: %s" % game._game_data['locations'][game.location]['Roles'])

    print("Players: ")
    for player in game.players:
        print("\tName: %s\t Role: %s" % (player.name, player.role))


game.join_player("Tymee")
game.join_player("Phil")
game.join_player("Paolo")
game.join_player("Fabio")
game.join_player("Jay")
game.join_player("Michaela")
start()
start()
start()
start()

game.leave_player("Tymee")
start()

listy = game.loc_list

print(listy)

from game import Game

game = Game()
game.join_player("bob")
game.join_player("phil")
game.join_player("other person")
game.start_game()

print("Location: %s" % game._game_data['locations'][game.location]['Location'])

game.leave_player("bob")

print("Players:")
for player in game.players:
    print("\tName:%s Role:%s" % (player.name, player.role))

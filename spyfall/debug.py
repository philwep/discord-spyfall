from game import Game

game = Game()
game.join_player("bob")
game.join_player("phil")
game.join_player("other person")
game.start_game()
print(game.location)
print(game.players)

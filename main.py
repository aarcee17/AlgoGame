from game import Game
from player import Player
from strategies import *


if __name__ == "__main__":
    players = [
        Player("Player 1", tactical_predict ),
        Player("Player 2", aggressive_predict),
        Player("Player 3", random_predict),
        Player("Player 4",conservative_predict)
    ]

    game = Game(players)
    game.start_game(50)  # Play 5 rounds
    print(game.__repr__())


import pickle as pickle

from Q_Learning_Tic_Tac_Toe import Game, HumanPlayer, QPlayer

Q = pickle.load(open("expert_bot.p", "rb"))

player1 = QPlayer(mark="X", epsilon=0.0)
player2 = HumanPlayer(mark="O")

game = Game(player1, player2, Q=Q)
game.play()



import pickle as pickle

from Q_Learning_Tic_Tac_Toe import Game, HumanPlayer, QPlayer

Q = pickle.load(open("expert_bot.p", "rb"))

player1 = HumanPlayer(mark="X")
player2 = QPlayer(mark="O", epsilon=0.0)

game = Game(player1, player2, Q=Q)
game.play()

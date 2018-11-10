import numpy as np
import tkinter as tk
import copy
import time
import sys
import os
import serial

ARD = serial.Serial("/dev/cu.usbmodem1421", 9600)
time.sleep(2)

class Game:
    def __init__(self, player1, player2, Q={}, alpha=0.3, gamma=0.9):

        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.other_player = player2
        self.empty_text = ""
        self.board = Board()

        self.Q_learn = True
        self._Q_learn = None

        if self.Q_learn:
            print('q_learn')
            self.Q = Q
            print(self.Q)
            self.alpha = alpha          # Learning rate
            self.gamma = gamma          # Discount rate
            self.share_Q_with_players()

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    @property
    def Q_learn(self):
        if self._Q_learn is not None:
            return self._Q_learn
        if isinstance(self.player1, QPlayer) or isinstance(self.player2, QPlayer):
            return True

    @Q_learn.setter
    def Q_learn(self, _Q_learn):
        self._Q_learn = _Q_learn

    def share_Q_with_players(self):             # The action value table Q is shared with the QPlayers to help them make their move decisions
        if isinstance(self.player1, QPlayer):
            self.player1.Q = self.Q
            print('shareq1')
        if isinstance(self.player2, QPlayer):
            self.player2.Q = self.Q
            print('shareq2')

    def dummy_callback(self):
        print('dummy_callback')
        randomplayer = RandomPlayer(mark="O")
        computer_move = randomplayer.get_move(self.board)
        self.handle_move(computer_move)
        self.board.send2board(computer_move, mark="O")
        human_move = self.get_button_fromboard()
        self.handle_move(human_move)
        return True

    def callback(self):
        print('callback')
        print(self.board.over())
        if self.board.over():
            print('board_over')
            return False
            #pass                # Do nothing if the game is already over
        else:
            if isinstance(self.current_player, ComputerPlayer) and isinstance(self.other_player, HumanPlayer):
                print('callbackpcvshuman')
                if True:
                    computer_move = self.current_player.get_move(self.board)
                    print('computer')
                    print(computer_move)
                    self.handle_move(computer_move)
                    self.board.send2board(computer_move, mark="O")
                    if not self.board.over():
                        human_move = self.get_button_fromboard()
                        self.handle_move(human_move)
                        return True
            elif isinstance(self.current_player, HumanPlayer) and isinstance(self.other_player, ComputerPlayer):
                print('callbackhumanvspc')
                computer_player = self.other_player
                if True:
                    human_move = self.get_button_fromboard()
                    self.handle_move(human_move)
                    if not self.board.over():               # Trigger the computer's next move
                        computer_move = computer_player.get_move(self.board)
                        print('computer')
                        print(computer_move)
                        self.handle_move(computer_move)
                        self.board.send2board(computer_move, mark="O")
                        return True

    def empty(self, button):
        return button["text"] == self.empty_text

    def get_button_fromboard(self):
        print('get_button')
        numbers2tuples = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0),
                          '8': (2, 1), '9': (2, 2)}
        answer = ARD.read()
        answer = answer.decode('ascii')
        move = numbers2tuples[answer]
        print(move)
        return move

    def get_move(self, button):
        print('get_move')
        info = button.grid_info()
        print(button)
        print(info)
        move = (int(info["row"]), int(info["column"])) # Get move coordinates from the button's metadata
        print(move)
        return move

    def handle_move(self, move):
        print('handle_move')
        i, j = move         # Get row and column number of the corresponding button
        self.board.place_mark(move, self.current_player.mark)
        if self.board.over():
            pass
        else:
            self.switch_players()

    def declare_outcome(self):
        if self.board.winner() is None:
            print("Cat's game.")
            time.sleep(2)
            self.reset()
        else:
            print(("The game is over. The player with mark {mark} won!".format(mark=self.current_player.mark)))
            time.sleep(2)
            self.send_winner(self.current_player.mark)
            time.sleep(2)
            self.reset()

    def send_winner(self,mark):
        if mark == "X":
            ARD.write(b'R')
        else:
            ARD.write(b'G')

    def reset(self):
        print("Resetting...")
        ARD.write(b'r')
        self.board = Board(grid=np.ones((3, 3)) * np.nan)
        self.current_player = self.player1
        self.other_player = self.player2
        self.play()

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.other_player = self.player1
        else:
            self.current_player = self.player1
            self.other_player = self.player2

    def play(self):
        print('play')
        if isinstance(self.player1, HumanPlayer) and isinstance(self.player2, HumanPlayer):
            pass        # For human vs. human, play relies on the callback from button presses
        elif isinstance(self.player1, HumanPlayer) and isinstance(self.player2, ComputerPlayer):
            print('humanvspc')
            flag = True
            first = True
            while flag:
                flag = self.callback()
            self.declare_outcome()
        elif isinstance(self.player1, ComputerPlayer) and isinstance(self.player2, HumanPlayer):
            print('pcvshuman')
            flag = True
            first = True
            while flag:
                if first:
                    flag = self.dummy_callback()
                    first = False
                else:
                    flag = self.callback()
            self.switch_players()
            self.declare_outcome()
        elif isinstance(self.player1, ComputerPlayer) and isinstance(self.player2, ComputerPlayer):
            #pass
            #first_computer_move = player1.get_move(self.board)
            #self.handle_move(first_computer_move)
            while not self.board.over():        # Make the two computer players play against each other without button presses
                self.play_turn()
                #time.sleep(2)

    def play_turn(self):
        print('play_turn')
        move = self.current_player.get_move(self.board)
        self.handle_move(move)

    def learn_Q(self, move):                        # If Q-learning is toggled on, "learn_Q" should be called after receiving a move from an instance of Player and before implementing the move (using Board's "place_mark" method)
        state_key = QPlayer.make_and_maybe_add_key(self.board, self.current_player.mark, self.Q)
        print('learn_Q')
        next_board = self.board.get_next_board(move, self.current_player.mark)
        reward = next_board.give_reward()
        next_state_key = QPlayer.make_and_maybe_add_key(next_board, self.other_player.mark, self.Q)
        if next_board.over():
            expected = reward
        else:
            next_Qs = self.Q[next_state_key]             # The Q values represent the expected future reward for player X for each available move in the next state (after the move has been made)
            if self.current_player.mark == "X":
                expected = reward + (self.gamma * min(next_Qs.values()))        # If the current player is X, the next player is O, and the move with the minimum Q value should be chosen according to our "sign convention"
            elif self.current_player.mark == "O":
                expected = reward + (self.gamma * max(next_Qs.values()))        # If the current player is O, the next player is X, and the move with the maximum Q vlue should be chosen
        change = self.alpha * (expected - self.Q[state_key][move])
        self.Q[state_key][move] += change


class Board:
    def __init__(self, grid=np.ones((3,3))*np.nan):
        self.grid = grid

    def winner(self):
        rows = [self.grid[i,:] for i in range(3)]
        cols = [self.grid[:,j] for j in range(3)]
        diag = [np.array([self.grid[i,i] for i in range(3)])]
        cross_diag = [np.array([self.grid[2-i,i] for i in range(3)])]
        lanes = np.concatenate((rows, cols, diag, cross_diag))      # A "lane" is defined as a row, column, diagonal, or cross-diagonal

        any_lane = lambda x: any([np.array_equal(lane, x) for lane in lanes])   # Returns true if any lane is equal to the input argument "x"
        if any_lane(np.ones(3)):
            return "X"
        elif any_lane(np.zeros(3)):
            return "O"

    def over(self):             # The game is over if there is a winner or if no squares remain empty (cat's game)
        return (not np.any(np.isnan(self.grid))) or (self.winner() is not None)

    def place_mark(self, move, mark):       # Place a mark on the board
        print('place_mark')
        num = Board.mark2num(mark)
        self.grid[tuple(move)] = num

    def send2board(self, move, mark):
        REDS = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        GREENS = np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
        tupla = tuple(move)
        i, j = tupla[0], tupla[1]
        if mark == "X":
            send = REDS[i][j]
        else:
            send = GREENS[i][j]
        bits = bytes(str(send), encoding="ascii")
        ARD.write(bits)

    @staticmethod
    def mark2num(mark):         # Convert's a player's mark to a number to be inserted in the Numpy array representing the board. The mark must be either "X" or "O".
        d = {"X": 1, "O": 0}
        return d[mark]

    def available_moves(self):
        return [(i,j) for i in range(3) for j in range(3) if np.isnan(self.grid[i][j])]

    def get_next_board(self, move, mark):
        time.sleep(.3)
        print('get_next_board')
        self.send2board(move, mark)
        next_board = copy.deepcopy(self)
        return next_board

    def make_key(self, mark):          # For Q-learning, returns a 10-character string representing the state of the board and the player whose turn it is
        fill_value = 9
        filled_grid = copy.deepcopy(self.grid)
        np.place(filled_grid, np.isnan(filled_grid), fill_value)
        return "".join(map(str, (list(map(int, filled_grid.flatten()))))) + mark

    def give_reward(self):                          # Assign a reward for the player with mark X in the current board position.
        if self.over():
            if self.winner() is not None:
                if self.winner() == "X":
                    return 1.0                      # Player X won -> positive reward
                elif self.winner() == "O":
                    return -1.0                     # Player O won -> negative reward
            else:
                return 0.5                          # A smaller positive reward for cat's game
        else:
            return 0.0                              # No reward if the game is not yet finished


class Player(object):
    def __init__(self, mark):
        self.mark = mark

    @property
    def opponent_mark(self):
        if self.mark == 'X':
            return 'O'
        elif self.mark == 'O':
            return 'X'
        else:
            print("The player's mark must be either 'X' or 'O'.")

class HumanPlayer(Player):
    pass

class ComputerPlayer(Player):
    pass

class RandomPlayer(ComputerPlayer):
    @staticmethod
    def get_move(board):
        moves = board.available_moves()
        if moves:   # If "moves" is not an empty list (as it would be if cat's game were reached)
            return moves[np.random.choice(len(moves))]    # Apply random selection to the index, as otherwise it will be seen as a 2D array

class THandPlayer(ComputerPlayer):
    def __init__(self, mark):
        super(THandPlayer, self).__init__(mark=mark)

    def get_move(self, board):
        moves = board.available_moves()
        if moves:
            for move in moves:
                if THandPlayer.next_move_winner(board, move, self.mark):
                    return move
                elif THandPlayer.next_move_winner(board, move, self.opponent_mark):
                    return move
            else:
                return RandomPlayer.get_move(board)

    @staticmethod
    def next_move_winner(board, move, mark):
        print('next_move_winner')
        return board.get_next_board(move, mark).winner() == mark


class QPlayer(ComputerPlayer):
    def __init__(self, mark, Q={}, epsilon=0.0):
        super(QPlayer, self).__init__(mark=mark)
        self.Q = Q
        self.epsilon = epsilon

    def get_move(self, board):
        if np.random.uniform() < self.epsilon:              # With probability epsilon, choose a move at random ("epsilon-greedy" exploration)
            return RandomPlayer.get_move(board)
        else:
            state_key = QPlayer.make_and_maybe_add_key(board, self.mark, self.Q)
            Qs = self.Q[state_key]

            if self.mark == "X":
                print('eligiendoX')
                return QPlayer.stochastic_argminmax(Qs, max)
            elif self.mark == "O":
                print('eligiendoO')
                return QPlayer.stochastic_argminmax(Qs, min)

    @staticmethod
    def make_and_maybe_add_key(board, mark, Q):     # Make a dictionary key for the current state (board + player turn) and if Q does not yet have it, add it to Q
        default_Qvalue = 1.0       # Encourages exploration
        state_key = board.make_key(mark)
        print(state_key)
        print(Q.get(state_key))
        if Q.get(state_key) is None:
            moves = board.available_moves()
            Q[state_key] = {move: default_Qvalue for move in moves}    # The available moves in each state are initially given a default value of zero
        return state_key

    @staticmethod
    def stochastic_argminmax(Qs, min_or_max):       # Determines either the argmin or argmax of the array Qs such that if there are 'ties', one is chosen at random
        min_or_maxQ = min_or_max(list(Qs.values()))
        if list(Qs.values()).count(min_or_maxQ) > 1:      # If there is more than one move corresponding to the maximum Q-value, choose one at random
            print(list(Qs.values()))
            best_options = [move for move in list(Qs.keys()) if Qs[move] == min_or_maxQ]
            print(best_options)
            move = best_options[np.random.choice(len(best_options))]
        else:
            move = min_or_max(Qs, key=Qs.get)
        return move

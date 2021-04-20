from tictactoe import player
from tictactoe import actions
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal

import math

X = "X"
O = "O"
EMPTY = None

# board = [[EMPTY, EMPTY, EMPTY],
#         [EMPTY, EMPTY, EMPTY],
#         [EMPTY, EMPTY, EMPTY]]

# board = [[EMPTY, EMPTY, EMPTY],
#         [EMPTY, X, O],
#         [EMPTY, EMPTY, EMPTY]]

board = [[X, X, O],
        [O, O, X],
        [X, X, O]]

action = (0,2)

# Test player method
# print(player(board))

# Test actions method
# print(actions(board))

# Test result method
# print(result(board, action))

# Test winner method
# print(winner(board))

# Test terminal method
# print(terminal(board))

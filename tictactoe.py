"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for value in row:
            if value == X:
                x_count += 1
            elif value == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    r_count = -1

    for row in board:
        r_count += 1
        c_count = -1
        for cell in row:
            c_count += 1
            if cell == EMPTY:
                moves.add((r_count, c_count))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    value = player(board)
    if action not in actions(board):
        raise ValueError
    
    new_state = copy.deepcopy(board)

    new_state[action[0]][action[1]] = value
    return new_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal checks
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != None:
            return row[0]

    # Vertical checks
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]

    # Diagonal checks
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    flag = False
    for row in board:
        for cell in row:
            if cell == None:
                flag = True
    if not flag:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def Max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, Min_value(result(board, action)))
    return v

def Min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, Max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None
    if player(board) == X:
        v = -math.inf
        for ac in actions(board):
            v = max(v, Min_value(result(board, ac)))
        for ac in actions(board):
            if v == Min_value(result(board, ac)):
                return ac
    else:
        v = math.inf
        for ac in actions(board):
            v = min(v, Max_value(result(board, ac)))
        for ac in actions(board):
            if v == Max_value(result(board, ac)):
                return ac

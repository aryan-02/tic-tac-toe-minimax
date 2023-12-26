"""
Tic Tac Toe Player
"""

import math

from copy import deepcopy

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
        for item in row:
            if item == X:
                x_count += 1
            elif item == O:
                o_count += 1
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action
    if board[i][j] is EMPTY:
        new_board[i][j] = player(board)
    else:
        raise ValueError("Invalid board state")
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if X won
    x_won = False
    for row in board:
        if row.count(X) == 3:
            x_won = True
    
    for c in range(3):
        x_count = 0
        for r in range(3):
            if board[r][c] == X:
                x_count += 1
        if x_count == 3:
            x_won = True
    
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        x_won = True
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        x_won = True
    
    # Check if O won
    o_won = False
    for row in board:
        if row.count(O) == 3:
            o_won = True
    
    for c in range(3):
        o_count = 0
        for r in range(3):
            if board[r][c] == O:
                o_count += 1
        if o_count == 3:
            o_won = True
    
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        o_won = True
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        o_won = True

    if x_won:
        return X
    elif o_won:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    empty_count = 0
    for row in board:
        for item in row:
            if item is EMPTY:
                empty_count += 1
    if empty_count == 0:
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

def board_value(board):
    if terminal(board):
        return utility(board)
    
    actions_possible = list(actions(board))
    boards_from_actions = [result(board, action) for action in actions_possible]
    values = [board_value(board) for board in boards_from_actions]
    if(player(board) == X):
        return max(values)
    else:
        return min(values)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actions_possible = list(actions(board))
    boards_from_actions = [result(board, action) for action in actions_possible]
    values = [board_value(board) for board in boards_from_actions]
    if(player(board) == X):
        return actions_possible[values.index(max(values))]
    else:
        return actions_possible[values.index(min(values))]
    

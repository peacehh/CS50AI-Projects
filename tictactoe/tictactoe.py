"""
Tic Tac Toe Player
"""

import math, copy

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
    c = 0
    for row in board: 
        c += row.count(EMPTY)
    return X if c%2==1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()  
    for x in range(3):
        for y in range(3):
            if board[y][x] == EMPTY:
                actions.add((y, x))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]: return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]: return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2] and board[1][1]:
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: return True

    for row in board:
        for square in row: 
            if square == EMPTY: return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    if winner(board) == O: return -1
    
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        for action in actions(board):
            if min_value(result(board, action)) == max_value(board): return action
    else:
        for action in actions(board):
            if max_value(result(board, action)) == min_value(board): return action

def min_value(board):
    v = 10
    if terminal(board): return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    v = -10
    if terminal(board): return utility(board)
    for action in actions(board): 
        v = max(v, min_value(result(board, action)))
    return v
        
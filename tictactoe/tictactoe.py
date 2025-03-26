"""
Tic Tac Toe Player
"""

import math

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
    cnt_x = 0
    cnt_o = 0
    for i in board :
        for j in i: 
            if j == X:
                cnt_x += 1
            elif j == O:
                cnt_o += 1
    if cnt_x == cnt_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("out of bounds")
    if board[i][j] != EMPTY:
        raise ValueError("already taken")

    i,j = action
    try_board = [row[:] for row in board]
    try_board[i][j] = player(board)
    return try_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if  row[0] != EMPTY and row[0] == row[1] == row[2]:
            return row[0]
    for hang in range(3):
        if board[0][hang] != EMPTY and board[0][hang] == board[1][hang] == board[2][hang]:
            return board[0][hang]
    if(board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if(board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    判断游戏是否结束
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    判断游戏结果
    """
    winner_one = winner(board)
    if winner_one == X:
        return 1
    elif winner_one == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    now_player = player(board)

    def max_val(board,alpha,beta):
        if terminal(board):
            return utility(board),None
        v = -math.inf
        best_action = None
        for act in actions(board):
            best_board = result(board,act)
            min_v = min_val(best_board,alpha,beta)[0]
            if min_v > v:
                v = min_v
                best_action = act
            alpha = max(alpha,v)
            if v >= beta:
                break
        return v,best_action
    def min_val(board,alpha,beta):
        if terminal(board):
            return utility(board),None
        v = math.inf
        best_action = None
        for act in actions(board):
            best_board = result(board,act)
            max_v = max_val(best_board,alpha ,beta)[0]
            if max_v < v:
                v = max_v
                best_action = act
            beta = min(beta,v)
            if v <= alpha:
                break
        return v,best_action
    alpha = -math.inf
    beta = math.inf
    if now_player == X:
        return max_val(board,alpha,beta)[1]
    else:       
        return min_val(board,alpha,beta)[1]

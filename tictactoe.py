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
    if board == initial_state():
        return X
    countX = 0
    countY = 0
    for row in board:
        for item in row:
            if item == X:
                countX+=1
            if item == O:
                countY+=1
    if (countX>countY):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board=board):
        return
    actions = []
    i = 0
    while i<=2:
        j=0
        while j<=2:
            if board[i][j] == EMPTY:
                actions.append((i,j))             
            j=j+1
        i=i+1
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board=board):
        return []
    (i,j) = action
    if (board[i][j] != EMPTY):
        raise Exception("Action not valid")
    
    temp = copy.deepcopy(board)
    turn_value = player(board)
    temp[i][j] = turn_value
    return temp

def checkrow(board,player):
    for row in board:
        if ((row[0] == player) and (row[1] == player) and (row[2] == player) ):
            return True
    return False

def checkcolumn(board,player):
    for i in range(len(board)):
        if ((board[0][i] == player) and (board[1][i] == player) and (board[2][i] == player) ):
            return True
    return False

def checkdiagonal(board,player):
    dmajCount = 0
    dminCount = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if ((i==j) and (board[i][j]==player)):
                dmajCount+=1
            if ((i+j==2) and (board[i][j]==player)):
                dminCount+=1
    if ((dmajCount == 3) or (dminCount == 3)):
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkrow(board,X) or checkcolumn(board,X) or checkdiagonal(board,X):
        return X
    if checkrow(board,O) or checkcolumn(board,O) or checkdiagonal(board,O):
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==None:
        i = 0
        while i<=2:
            j=0
            while j<=2:
                if board[i][j] == EMPTY:
                    return False           
                j=j+1
            i=i+1
        return True
    else:
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (terminal(board)):
        if (winner(board=board)==X):
            return 1
        if (winner(board=board)==O):
            return -1
        if  (winner(board=board)==None):
            return 0

def max_Value(board):
    if terminal(board=board):
        return utility(board=board)
    v =-math.inf
    possible_actions = actions(board)
    if (len(possible_actions) > 0):
        for act in possible_actions:
            v = max(v,min_Value(result(board,act)))
        return v


def min_Value(board):
    if terminal(board=board):
        return utility(board=board)
    v =math.inf
    possible_actions = actions(board)
    if (len(possible_actions) > 0):
        for act in possible_actions:
            v = min(v,max_Value(result(board,act)))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    next_player=player(board)
    all_actions = actions(board)
    possible_actions = []
    if (next_player == X):

        for action in all_actions:
            next_state = result(board,action)
            min_value = max_Value(next_state)
            possible_actions.append((min_value,action))
        res = -math.inf
        maxFound = False
        for (val,action) in possible_actions:
            if (res<val):
                res = val
                maxFound = True
                resultAction = action
        if maxFound:        
            return resultAction
    
    if (next_player == O):

        for action in all_actions:
            next_state = result(board,action)
            max_value = max_Value(next_state)
            possible_actions.append((max_value,action))
        res = math.inf
        minFound = False
        for (val,action) in possible_actions:
            if (res>val):
                res = val
                minFound = True
                resultAction = action
        if minFound:        
            return resultAction
    
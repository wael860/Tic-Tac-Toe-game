"""
Tic Tac Toe Player
"""

import math
import copy

from sqlalchemy import true

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
    x=0
    o=0
    for row_ in board:
        x+=row_.count("X")
        o+=row_.count("O")
    if(x>o):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=list()
    action_=tuple()
    for i in range (0, 3):
        for j in range (0, 3):
            if(board[i][j]==EMPTY):
                action_=(i,j)
                possible_actions.append(action_)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        dummy_board=copy.deepcopy(board)
        i=action[0]
        j=action[1]
        if(board[i][j]==EMPTY):
            dummy_board[i][j]=player(dummy_board)
        else:
            raise Exception ("XXXX")
    except Exception as error:
            print('Caught this error: ' + repr(error))
    return dummy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i[0] == i[1] and i[0] == i[2]:

            return i[0]   

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        #return True
    #else:
        #return False
    value=winner(board)
    if value==O or value==X:
        return True
    count=actions(board)
    if len(count)==0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #Assuming terminal is TRUE
    if(winner(board)=="X"):
        return 1
    elif(winner(board)=="O"):
        return -1
    else:
        return 0
def minimax(board):
    if(terminal(board)):
        return None
    if(player(board)=="X"):
        if(len(actions(board))==9):
            return (0,0) 
        v,act=maximize(board)
        return act
    elif(player(board)=="O"):
        if(len(actions(board))==9):
            return (0,0) 
        v,act =minimize(board)
        return act
    return None

def maximize(board):
    if(terminal(board)):
        return  utility(board), EMPTY
    v_=-2
    _act=EMPTY
    for act in actions(board):#Test All the moves of X
        v,act_=minimize(result(board,act))
        if(v>v_):
            v_=v
            _act=act
            if(v_>0):
                return v_,_act
    return v_,_act
            
def minimize(board):
    if(terminal(board)):
        return  utility(board), EMPTY
    v_=2
    _act=EMPTY
    for act in actions(board):#Test All the moves of O
        v,act_=maximize(result(board,act))
        if(v<v_):
            v_=v
            _act=act
            if(v_<0):
                return v_,_act
    return v_,_act
    

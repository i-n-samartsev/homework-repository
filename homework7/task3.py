"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "x":
            return "x wins!"
        if board[i][0] == board[i][1] == board[i][2] == "o":
            return "o wins!"
        if board[0][i] == board[1][i] == board[2][i] == "x":
            return "x wins!"
        if board[0][i] == board[1][i] == board[2][i] == "o":
            return "o wins!"

    if board[0][0] == board[1][1] == board[2][2] == "x":
        return "x wins!"
    if board[0][0] == board[1][1] == board[2][2] == "o":
        return "o wins!"
    if board[0][0] == board[1][1] == board[2][2] == "x":
        return "x wins!"
    if board[0][2] == board[1][1] == board[2][0] == "o":
        return "o wins!"

    is_draw = True
    for line in board:
        if line.count("-") != 0:
            is_draw = False
            break
    if is_draw:
        return "draw!"
    else:
        return "unfinished"

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
    Return value should be "unfinished!"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    len_board = len(board)
    for i in range(len_board):
        if board[i].count("x") == len(board[i]):
            return "x wins!"
        if board[i].count("o") == len(board[i]):
            return "o wins!"
        if all([board[k][i] == "x" for k in range(len_board)]):
            return "x wins!"
        if all([board[k][i] == "o" for k in range(len_board)]):
            return "o wins!"

    if all([board[i][i] == "x" for i in range(len_board)]):
        return "x wins!"
    if all([board[i][i] == "o" for i in range(len_board)]):
        return "o wins!"
    if all([board[i][len_board - i - 1] == "x" for i in range(len_board)]):
        return "x wins!"
    if all([board[i][len_board - i - 1] == "o" for i in range(len_board)]):
        return "o wins!"

    for line in board:
        if line.count("-") != 0:
            return "unfinished!"
    return "draw!"

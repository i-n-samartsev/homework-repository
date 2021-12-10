import pytest

from homework7.hw3 import (BothVictoryError, IncorrectBoardSizeError,
                           IncorrectSymbolsError, TicTacToeBoard)


@pytest.fixture(scope='function')
def x_victory_board():
    yield TicTacToeBoard([['x', '-', 'x'],
                          ['-', 'x', 'o'],
                          ['x', 'o', 'o']])


@pytest.fixture(scope='function')
def o_victory_board():
    yield TicTacToeBoard([['o', '-', 'o'],
                          ['-', 'o', 'x'],
                          ['x', 'x', 'o']])


@pytest.fixture(scope='function')
def unfinished_board():
    yield TicTacToeBoard([['-', 'o', '-'],
                          ['x', 'x', 'o'],
                          ['-', 'o', '-']])


@pytest.fixture(scope='function')
def draw_board():
    yield TicTacToeBoard([['o', 'o', 'x', 'x'],
                          ['o', 'x', 'o', 'x'],
                          ['x', 'o', 'x', 'o'],
                          ['x', 'x', 'o', 'o']])


@pytest.fixture(scope='function')
def both_victory_board():
    yield TicTacToeBoard([['x', 'x', 'x'],
                          ['o', 'o', 'o'],
                          ['x', 'o', 'o']])


def test_tic_tac_toe_return_x_victory(x_victory_board):
    assert x_victory_board.check_winner() == 'x wins'


def test_tic_tac_toe_return_o_victory(o_victory_board):
    assert o_victory_board.check_winner() == 'o wins'


def test_tic_tac_toe_return_draw(draw_board):
    assert draw_board.check_winner() == 'draw'


def test_tic_tac_toe_return_unfinished(unfinished_board):
    assert unfinished_board.check_winner() == 'unfinished'


def test_tic_tac_toe_check_line_return_x_victory():
    assert TicTacToeBoard.check_line(['x', 'x', 'x', 'x']) == 'x wins'


def test_tic_tac_toe_check_line_return_o_victory():
    assert TicTacToeBoard.check_line(['o', 'o']) == 'o wins'


def test_tic_tac_toe_check_line_return_draw():
    assert TicTacToeBoard.check_line(['x', 'o', 'x']) == 'draw'


def test_tic_tac_toe_check_line_return_unfinished():
    assert TicTacToeBoard.check_line(['-', 'x', 'o']) == 'unfinished'


def test_tic_tac_toe_get_horizontal_line(draw_board):
    assert draw_board.get_horizontal_line(2) == ['o', 'x', 'o', 'x']


def test_tic_tac_toe_get_vertical_line(draw_board):
    assert draw_board.get_vertical_line(4) == ['x', 'x', 'o', 'o']


def test_tic_tac_toe_get_main_diagonal(draw_board):
    assert draw_board.get_main_diagonal() == ['o', 'x', 'x', 'o']


def test_tic_tac_toe_get_side_diagonal(draw_board):
    assert draw_board.get_side_diagonal() == ['x', 'o', 'o', 'x']


def test_tic_tac_toe_raises_both_victory_error(both_victory_board):
    with pytest.raises(BothVictoryError, match='Both players'):
        both_victory_board.check_winner()


def test_tic_tac_toe_raises_incorrect_size_error():
    with pytest.raises(IncorrectBoardSizeError, match='square'):
        TicTacToeBoard([['o', 'x', 'o'],
                        ['x', 'x', 'o', '-'],
                        ['o', 'o', 'x']])


def test_tic_tac_toe_raises_incorrect_symbols_error():
    with pytest.raises(IncorrectSymbolsError, match='Only'):
        TicTacToeBoard([['o', 'x', 'o'],
                        ['x', '123', 'o'],
                        ['aba', 'o', 'x']])

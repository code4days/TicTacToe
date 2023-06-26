from unittest.mock import patch

import pytest

from tic_tac_toe.tic_tac_toe import check_winner, get_move, is_board_full, is_valid_move


@pytest.fixture
def get_full_board():
    return [
        ["x", "o", "x"],
        ["o", "x", "o"],
        ["o", "o", "x"],
    ]


@pytest.fixture
def get_half_full_board():
    return [
        ["x", "o", "x"],
        ["o", "x", "o"],
        ["o", "o", ""],
    ]


def test_check_winner(get_full_board, get_half_full_board):
    full_board = get_full_board
    half_full_board = get_half_full_board
    assert check_winner(full_board, "x", 0, 0) == True
    assert check_winner(full_board, "o", 0, 1) == False
    assert check_winner(half_full_board, "x", 0, 0) == False


def test_get_move():
    # mock user input
    with patch("builtins.input", return_value="0 0"):
        assert get_move() == (0, 0)


def test_is_valid_move(get_half_full_board):
    half_full_board = get_half_full_board
    assert is_valid_move(half_full_board, 0, 0) == False
    assert is_valid_move(half_full_board, 2, 2) == True


def test_is_board_full():
    assert is_board_full(9) == True
    assert is_board_full(8) == False

import pytest
from streamlit_app.app import (
    determine_rpsls_winner,
    check_ttt_winner,
    check_ttt_draw,
    check_battleship_winner
)

# Pruebas para Rock Paper Scissors Lizard Spock
def test_rpsls_winner():
    # Prueba victoria de Rock sobre Scissors
    assert determine_rpsls_winner("Rock", "Scissors") == "You win!"
    # Prueba victoria de Rock sobre Lizard
    assert determine_rpsls_winner("Rock", "Lizard") == "You win!"
    # Prueba empate
    assert determine_rpsls_winner("Rock", "Rock") == "It's a draw!"
    # Prueba derrota
    assert determine_rpsls_winner("Rock", "Paper") == "You lose!"

# Pruebas para Tic Tac Toe
def test_ttt_winner():
    # Prueba victoria en fila
    board_row = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert check_ttt_winner(board_row, 'X') == True
    
    # Prueba victoria en columna
    board_col = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
    assert check_ttt_winner(board_col, 'O') == True
    
    # Prueba victoria en diagonal
    board_diag = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert check_ttt_winner(board_diag, 'X') == True

def test_ttt_draw():
    # Prueba tablero lleno
    full_board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
    assert check_ttt_draw(full_board) == True
    
    # Prueba tablero no lleno
    partial_board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', ' ']
    assert check_ttt_draw(partial_board) == False

# Pruebas para Battleship
def test_battleship_winner():
    # Prueba tablero con barcos
    board_with_ships = [
        ['🚢', ' ', ' ', ' ', ' '],
        [' ', '🚢', ' ', ' ', ' '],
        [' ', ' ', '🚢', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert check_battleship_winner(board_with_ships) == False
    
    # Prueba tablero sin barcos (victoria)
    empty_board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    assert check_battleship_winner(empty_board) == True 
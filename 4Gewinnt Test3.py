import numpy as np

# Spielbrett-Größe
ROWS = 6
COLS = 7

# Spieler-IDs
PLAYER1 = 1
PLAYER2 = 2

# Spielbrett-Initialisierung
board = np.zeros((ROWS, COLS), dtype=int)

# Funktion zur Anzeige des Spielbretts im Terminal
def print_board(board):
    print("|_0_|_1_|_2_|_3_|_4_|_5_|_6_|\n" + 
          "|___|___|___|___|___|___|___|")
    for row in range(ROWS):
        row_str = "|"
        for col in range(COLS):
            if board[row][col] == PLAYER1:
                row_str += "_X_|"
            elif board[row][col] == PLAYER2:
                row_str += "_O_|"
            else:
                row_str += "___|"
        print(row_str)

# Funktion zur Überprüfung, ob ein Spielzug gültig ist
def is_valid_move(board, col):
    return board[ROWS-1][col] == 0

# Funktion zur Durchführung eines Spielzugs
def make_move(board, col, player):
    for row in range(ROWS):
        if board[row][col] == 0:
            board[row][col] = player
            return

# Funktion zur Überprüfung, ob das Spiel beendet ist
def is_game_over(board):
    # Überprüfen der horizontalen Linien
    for row in range(ROWS):
        for col in range(COLS-3):
            if (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]) and (board[row][col] != 0):
                return True

    # Überprüfen der vertikalen Linien
    for row in range(ROWS-3):
        for col in range(COLS):
            if (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]) and (board[row][col] != 0):
                return True

    # Überprüfen der Diagonal

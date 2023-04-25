def IsWin(board):
    # horizontale Linie:
    for row in range(row):
        for col in range(COLS-3):
            if (board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]) and (board[row][col] != 0):
                return True

    # vertikale Linie:
    for row in range(ROWS-3):
        for col in range(COLS):
            if (board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]) and (board[row][col] != 0):
                return True
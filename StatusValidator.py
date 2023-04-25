class StatusValidator:
    def __init__(self) -> None:
        pass

    def is_win_waagerecht(self, board, column_number, current_player) -> bool:
        for column_number in board:#oder rowString
            if(column_number == current_player.player_symbol and [column_number +1] and [column_number -1] and [column_number +2] and [column_number -2]):
                print(board)
                print(f"{current_player}, you win.")

    def is_win_senkrecht(self, board, column_number, current_player) -> bool:
        for cell in board:
            if(column_number == current_player.player_symbol and [cell +1] and [cell -1] and [cell +2] and [cell -2]):
                print(f"{current_player}, you win.")

    def Validator_Board(self) -> None:
        self.is_win_waagerecht()
        self.is_win_senkrecht()
        self.is_win(self)
        # self.is_win_diagonal()
        # self.is_win_draw()

#     def is_win_diagonal(self, board) -> bool:
#         for row in board:
#             if()

# # Alle Felder voll!
#     def is_draw(self, board) -> bool:
#         for row in board:
#             if()

    def is_win(rowString, cell, column_number, current_player, board) -> bool:
        for row in range(rowString-3):
            for row in range(row):
                            if(board[row][cell] == column_number and board[row-1][cell+1] == column_number and board[row-2][cell+2] == current_player and board[row-3][cell+3] == current_player):
                                print("nice") 


    def cell_is_checked(self, board, current_player, row, column) -> bool:
        cell =  board[row][column]
        isChecked = current_player in cell #cell.contains player symbol
        return isChecked
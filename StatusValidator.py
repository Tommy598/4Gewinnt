class StatusValidator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def is_win_sequence(sequence_array, player_symbol) -> bool:
        player_symbol_array = []
        for cell in sequence_array:
            if player_symbol in cell:
                player_symbol_array.append(player_symbol)
        if player_symbol in player_symbol_array * 4:
            return True
        
        return False

    @staticmethod
    def is_vertical_win(board, current_player) -> bool:
        for row in range (7): 
            for column in range (4):
                sequence_array = []
                for cell in range (4):
                    sequence_array.append(board[row][cell + column])
                    #print(board[row][cell + column], end="")
                    if StatusValidator.is_win_sequence(sequence_array, current_player.player_symbol):
                        return True
        return False
    # irgendwas mit der Schleife ist falsch!!!



#     def is_win_waagerecht(self, board, column_number, current_player) -> bool:
#         for column_number in board:#oder rowString
#             if(column_number == current_player.player_symbol and [column_number +1] and [column_number -1] and [column_number +2] and [column_number -2]):
#                 print(board)
#                 print(f"{current_player}, you win.")

#     def is_win_senkrecht(self, board, column_number, current_player) -> bool:
#         for cell in board:
#             if(column_number == current_player.player_symbol and [cell +1] and [cell -1] and [cell +2] and [cell -2]):
#                 print(f"{current_player}, you win.")

#     def is_win_diagonal(self, board) -> bool:
#         for row in board:
#             if()

#     #Alle Felder voll!
#     def is_draw(self, board) -> bool:
#         for row in board:
#             if()

#     def is_win(rowString, cell, column_number, current_player, board) -> bool:
#         for row in range(rowString-3):
#             for row in range(row):
#                             if(board[row][cell] == column_number and board[row-1][cell+1] == column_number and board[row-2][cell+2] == current_player and board[row-3][cell+3] == current_player):
#                                 print("nice")
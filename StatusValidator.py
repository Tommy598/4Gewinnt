from Board import Board

class StatusValidatior:
    def __init__(self) -> None:
        pass

    def is_win(self, column_number, current_player, board) -> bool:
        for row in board:     #oder rowString
            #print(board)
            if(column_number == current_player.player_symbol and [row +1] and [row -1] and [row +2] and [row -2]):
                print(f"{current_player}, you win.")

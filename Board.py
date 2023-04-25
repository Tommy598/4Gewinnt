#from Player import Player
class Board:
    def __init__(self):
        self.board = self.create_board()
    
    def create_board(self) -> list[list[str]]:  
        list_Board = [["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|_|","_|","_|","_|","_|","_|","_|"],
                      ["|1|2|3|4|5|6|7|"]]
        return list_Board

    def show_board(self) -> None:
        for row in self.board:
            for cell in row:
                print(cell, end="")
            print()

    def is_valid_turn(self, column_number: int) -> bool:
        # Spalte voll?
        if '_' not in self.board[0][column_number]:
            return False
        return True
        
    def add_coin_to_board(self, player_symbol, column_number:int) -> None:
        row_index = -2
        while row_index > -9:
            if '_' in self.board[row_index][column_number]:
                self.board[row_index][column_number] = self.board[row_index][column_number].replace('_', player_symbol)
                return

            row_index -= 1
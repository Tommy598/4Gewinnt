from Player import Player
from StatusValidator import StatusValidator
from Board import Board

class MainGame:
    def __init__(self) -> None:
        pass

    def get_user_name(self, player_number) -> str:
        return input(f"Player {player_number}: Please enter your name: ")

    def prepare_game(self) -> None:
        player_number = 1
        self.player_one = Player(self.get_user_name(player_number), "O")
        player_number = 2
        self.player_two = Player(self.get_user_name(player_number), "X")

    def Turn(self, board, current_player) -> None:
        print(f"{current_player.player_name}: ")
        column_number = self.GetRowInput(board)
        board.add_coin_to_board(current_player.player_symbol, column_number)
        if StatusValidator.is_vertical_win(board.board, current_player):
            if (is_vertical_win):
                win
                print winner
                play again?
            else
                return
            print("You´re the winner!")
            StatusValidator.is_vertical_win()
        # StatusValidator.Validate_Board(self, current_player)
        # StatusValidator.is_win_waagerecht(self, board, current_player, column_number)
        # StatusValidator.is_win_senkrecht(self, board, current_player, column_number)
        # StatusValidator.is_win_horizontal(self, row, cell_is_checked, current_player)
        # StatusValidator.is_win_vertical(self, row, cell_is_checked, current_player)

    def GetRowInput(self, board) -> int:
        while True:
            while True:
                try:
                    column_number = int(input("Select a row to put your coin (1-7): ")) - 1
                    if 0 <= column_number and column_number <= 6:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            if not '_' in board.board[0][column_number]:
                print(f"Full column, please enter another number than {column_number + 1}")
                continue

            return column_number

    def Round(self, board, round_number) -> None:
        current_player = self.player_one
        print("\nRound " + str(round_number) + ": ")
        self.Turn(board, current_player)
        board.show_board()
        current_player = self.player_two
        print("\nRound " + str(round_number) + ": ")
        self.Turn(board, current_player)
        board.show_board()

    def Play(self, board):
        round_number = 0
        while True:
            self.Round(board, round_number)
            round_number += 1
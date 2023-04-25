#startpunkt des Programms
from MainGame import MainGame
from Player import Player
from Board import Board
#from StatusValidator import StatusValidatior

def main() -> None:
    game = MainGame()
    game.prepare_game()
    board = Board()
    board.show_board()
    game.Play(board)

if __name__ == "__main__":
    main()

# Schritt 2.3 Kontrolle Funktioniert nicht. Mehrere Fehler.
import os

from board import Board
from player import ManualPlayer, MiniMaxPlayer, Player

DEPTH_LIMIT = 5

if __name__ == "__main__":
    board = Board()
    player1: Player = MiniMaxPlayer(True, DEPTH_LIMIT) if input(
        "Selecione modo de jogo para o jogador 1 (1 - Humano, 2 - Máquina): ") == "2" else ManualPlayer(True)
    player2: Player = MiniMaxPlayer(False, DEPTH_LIMIT) if input(
        "Selecione modo de jogo para o jogador 2 (1 - Humano, 2 - Máquina): ") == "2" else ManualPlayer(False)
    isPlayer1Turn = False

    while (True):
        os.system('cls' if os.name == 'nt' else 'clear')
        board.print()
        isOver = board.isTerminal()
        if isOver == 0:
            print("Empate.")
            break
        elif isOver == 1:
            print("Jogador 1 (O) ganhou")
            break
        elif isOver == 2:
            print("Jogador 2 (X) ganhou")
            break
        else:
            isPlayer1Turn = not isPlayer1Turn

        if isPlayer1Turn:
            move = player1.findMove(board)
        else:
            move = player2.findMove(board)
        board.makeMove(move)

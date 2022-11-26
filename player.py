import math

from board import Board


class Player:
    def __init__(self, isPlayerOne, depthLimit=5):
        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    def findMove(self, board: Board):
        pass


class MiniMaxPlayer(Player):
    def findMove(self, board):
        print("Calculando melhor jogada...")
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        return move

    # Atuador: minimax
    def miniMax(self, board, depth, isPlayerOne):
        if depth == 0:
            result = self.getReward(board), -1
            return result

        if isPlayerOne:
            bestScore = -math.inf
            def shouldReplace(x): return x > bestScore
        else:
            bestScore = math.inf
            # Inverte a função de comparação para o jogador 2
            # (maximizar o score do jogador 2 é minimizar o score do jogador 1)
            def shouldReplace(x): return x < bestScore
        bestMove = -1
        # Sensores: children: gera lista de possíveis jogadas a partir do estado atual
        children = board.children()
        for child in children:
            move, childboard = child
            tempScore = self.miniMax(childboard, depth-1, not isPlayerOne)[0]
            # Caso o valor da jogada seja melhor que o melhor valor encontrado até o momento, substitui
            # o melhor valor encontrado até o momento
            if shouldReplace(tempScore):
                bestScore = tempScore
                bestMove = move
        return bestScore, bestMove

    # Sensores: getReward: retorna o valor de recompensa do estado atual
    # Aumenta o valor de recompensa para o jogador que está ganhando
    # Quando maior o número de peças em sequência, maior o valor de recompensa
    # Quando o jogador inimigo tem mais peças em sequência, diminui o valor de recompensa
    def getReward(self, board: Board):
        reward = 0
        currentBoard = board.board
        for x in range(0, board.WIDTH):
            for y in range(0, board.HEIGHT):
                # Horizontal (x)
                try:
                    if currentBoard[x][y] == currentBoard[x + 1][y] == 0:
                        reward += 1
                    if currentBoard[x][y] == currentBoard[x + 1][y] == currentBoard[x + 2][y] == 0:
                        reward += 2
                    if currentBoard[x][y] == currentBoard[x+1][y] == currentBoard[x+2][y] == currentBoard[x+3][y] == 0:
                        reward += 3

                    if currentBoard[x][y] == currentBoard[x + 1][y] == 1:
                        reward -= 1
                    if currentBoard[x][y] == currentBoard[x + 1][y] == currentBoard[x + 2][y] == 1:
                        reward -= 2
                    if currentBoard[x][y] == currentBoard[x+1][y] == currentBoard[x+2][y] == currentBoard[x+3][y] == 1:
                        reward -= 3
                except IndexError:
                    pass

                # Vertical (y)
                try:
                    if currentBoard[x][y] == currentBoard[x][y + 1] == 0:
                        reward += 1
                    if currentBoard[x][y] == currentBoard[x][y + 1] == currentBoard[x][y + 2] == 0:
                        reward += 2
                    if currentBoard[x][y] == currentBoard[x][y+1] == currentBoard[x][y+2] == currentBoard[x][y+3] == 0:
                        reward += 3

                    if currentBoard[x][y] == currentBoard[x][y + 1] == 1:
                        reward -= 1
                    if currentBoard[x][y] == currentBoard[x][y + 1] == currentBoard[x][y + 2] == 1:
                        reward -= 2
                    if currentBoard[x][y] == currentBoard[x][y+1] == currentBoard[x][y+2] == currentBoard[x][y+3] == 1:
                        reward -= 3
                except IndexError:
                    pass

                # Diagonal (x+y)
                try:
                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x + 1][y + 1] == 0:
                        reward += 1
                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x + 1][y + 1] == currentBoard[x + 2][y + 2] == 0:
                        reward += 2
                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x+1][y + 1] == currentBoard[x+2][y + 2] \
                            == currentBoard[x+3][y + 3] == 0:
                        reward += 3

                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x + 1][y + 1] == 1:
                        reward -= 1
                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x + 1][y + 1] == currentBoard[x + 2][y + 2] == 1:
                        reward -= 2
                    if not y + 3 > board.HEIGHT and currentBoard[x][y] == currentBoard[x+1][y + 1] == currentBoard[x+2][y + 2] \
                            == currentBoard[x+3][y + 3] == 1:
                        reward -= 3
                except IndexError:
                    pass

                # Diagonal (x-y)
                try:
                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == 0:
                        reward += 1
                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == currentBoard[x+2][y - 2] == 0:
                        reward += 2
                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == currentBoard[x+2][y - 2] \
                            == currentBoard[x+3][y - 3] == 0:
                        reward += 3

                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == 1:
                        reward -= 1
                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == currentBoard[x+2][y - 2] == 1:
                        reward -= 2
                    if not y - 3 < 0 and currentBoard[x][y] == currentBoard[x+1][y - 1] == currentBoard[x+2][y - 2] \
                            == currentBoard[x+3][y - 3] == 1:
                        reward -= 3
                except IndexError:
                    pass
        return reward


class ManualPlayer(Player):
    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " " + \
                (str(c + 1) if len(board.board[c]) < 6 else ' ') + "  "
        print(opts)

        col = input(
            "Colocar " + ('O' if self.isPlayerOne else 'X') + " na coluna: ")
        col = int(col) - 1
        return col

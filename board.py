class Board(object):
    HEIGHT = 6
    WIDTH = 7

    def __init__(self, orig=None):
        if (orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return
        else:
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            return

    def makeMove(self, column: int):
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)

    # Sensor: retorna uma lista com todas as jogadas possíveis
    def children(self) -> list:
        children = []
        for x in range(7):
            if len(self.board[x]) < 6:
                child = Board(self)
                child.makeMove(x)
                children.append((x, child))
        return children

    # Retorna
    # -1 se o jogo não acabou
    # 0 se o jogo empatou
    # 1 se o jogador 1 ganhou
    # 2 se o jogador 2 ganhou
    def isTerminal(self) -> int:
        for i in range(0, self.WIDTH):
            for j in range(0, self.HEIGHT):
                try:
                    if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j + 3 > self.HEIGHT and self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j - 3 < 0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass
        if self.isFull():
            return 0
        return -1

    def isFull(self):
        return self.numMoves == 42

    def print(self):
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + \
                        ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)
        print("Total de jogadas:", self.numMoves)

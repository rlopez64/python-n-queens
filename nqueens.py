class Queen:
    def __init__(self, x: int = -1, y: int = -1):
        self.x = x
        self.y = y

    def attacks(self, other) -> bool:
        slope = abs((other.y - self.y) / (other.x - self.x))
        if self.x == other.x:
            return True
        elif self.y == other.y:
            return True
        elif slope == 1:
            return True
        else:
            return False


class Board:
    def __init__(self, n: int):
        self.board = []
        self.n = n
        for _ in range(n):
            self.board.append(Queen())

    def place_queen(self, index: int, queen: Queen):
        self.board[index] = queen

    def remove_queen(self, index: int):
        self.board[index] = Queen()

    def valid_placement(self, queen: Queen) -> bool:
        index = queen.x
        for i in range(index):
            prev_queen = self.board[i]
            if queen.attacks(prev_queen):
                return False
        return True

    def __str__(self):
        string = ""
        for x in range(self.n):
            queen = self.board[x]
            for y in range(self.n):
                if queen.y == y:
                    string += "♛ "
                else:
                    string += "- "
            string += "\n"
        return string


class NQueensSolution:

    def __init__(self, n: int) -> None:
        self.board = Board(n)
        self.solve(0)

    def solve(self, index) -> None:
        # TODO: Solve with recursion

        pass


if __name__ == "__main__":
    n_queens = NQueensSolution(4)
    print(n_queens.board)

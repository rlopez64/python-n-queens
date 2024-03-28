class Queen():
    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y

    def attacks(self, other):
        slope = abs((other.y - self.y) / (other.x - self.x))
        print(slope)
        if self.x == other.x:
            return True
        elif self.y == other.y:
            return True
        elif slope == 1:
            return True
        else:
            return False
        
        
        

class Board():
    def __init__(self, n):
        self.board = []
        self.n = n
        for _ in range(n):
            self.board.append(Queen())
    
    def place_queen(self, index, queen):
        self.board[index] = queen

    
    def __str__(self):
        string = ''
        for x in range(self.n):
            queen = self.board[x]
            for y in range(self.n):
                if queen.y == y:
                    string += '♛ '
                else:
                    string += '- '
            string += '\n'
        return string

    

if __name__ == '__main__':
    # board = Board(4)
    # board.place_queen(0, Queen(0, 1))
    # board.place_queen(1, Queen(1, 3))
    # board.place_queen(2, Queen(2, 0))
    # board.place_queen(3, Queen(3, 2))
    # print(board)
    q1 = Queen(2,3)
    q2 = Queen(3,2)

    print(q1.attacks(q2))


# Initialize array of size N to hold queens
#   Queens are original set to -1, -1

# For each queen set it to a correct spot
#   New queen does not attack previous queens

#
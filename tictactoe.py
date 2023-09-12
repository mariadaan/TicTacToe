class Board(object):
    def __init__(self):
        self.state = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def print_board(self):
        print()
        for i in range(3):
            print(f" {self.state[i][0]} | {self.state[i][1]} | {self.state[i][2]} ")
            if i < 2:
                print("---|---|---")
        print()

    def make_move(self, symbol = str, pos = str):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == pos:
                    self.state[i][j] = symbol
                    return
        raise Exception("Input must be an unused position on the board!")

    def __str__(self):
        pass


class Game(object):
    def __init__(self, board = Board):
        self.finished = False
        self.playerO_won = False
        self.player1_won = False
        self.board = board
    
    def play(self):
        board.print_board()



if __name__ == "__main__":
    board = Board()
    game = Game()
    game.play()
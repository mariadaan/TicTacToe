class Board(object):
    def __init__(self):
        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def print_board(self):
        print()
        for i in range(3):
            print(f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")
            if i < 2:
                print("---|---|---")
        print()

    def make_move(self, symbol = str, pos = str):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == pos:
                    self.board[i][j] = symbol
                    return
        raise Exception("Input must be an unused position on the board!")

    def has_winner(self):
        return False

    def __str__(self):
        pass


class Game(object):
    def __init__(self, board = Board):
        self.finished = False
        self.board = board
    
    def play(self):
        print("Welcome to this game of Tic Tac Toe!\n"
              "The rules are simple: the player who has 3 in a row first, wins.\n"
              "The first player may now choose a position from 1 to 9 to make their first move.")

        symbol = 'X'
        while (self.finished == False):
            board.print_board()
            pos = input(f"{symbol} pick a position: ")
            try:
                board.make_move(symbol, pos)
                symbol = 'O' if symbol == 'X' else 'X'
                if (board.has_winner()):
                    print(f"Player {symbol} has won!")
                    return
            except Exception as e:
                print(e)
                pos = input("Position: ")
                self.finished = True



if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.play()
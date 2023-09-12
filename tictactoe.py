class Board(object):
    def __init__(self):
        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def print_board(self):
        print()
        for i in range(len(self.board)):
            if i > 0:
                print("━━━╋━━━╋━━━")
            print(f" {self.board[i][0]} ┃ {self.board[i][1]} ┃ {self.board[i][2]} ")
        print()

    def make_move(self, symbol: str, pos: str):
        pos_int = int(pos) - 1
        row = pos_int // 3
        col = pos_int % 3
        if not 0 <= pos_int <= 8 or self.board[row][col] == 'O' or self.board[row][col] == 'X':
            raise Exception("Input must be an unused position on the board!")
        self.board[row][col] = symbol

    def has_won(self, symbol: str):
        for row in self.board:
            if row[0] == row[1] == row[2] == symbol:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol):
            return True
        return False

    def is_full(self):
        for row in self.board:
            for cell in row:
                if not (cell == 'O' or cell == 'X'):
                    return False
        return True


class Game(object):
    def __init__(self, board: Board):
        self.board = board
    
    def play(self):
        print("Welcome to this game of Tic Tac Toe!\n"
              "The rules are simple: the player who has 3 in a row first, wins.\n"
              "The first player may now choose a position from 1 to 9 to make their first move.")

        board.print_board()
        symbol = 'X'
        while True:
            pos = input(f"{symbol} pick a position: ")
            try:
                board.make_move(symbol, pos)
                board.print_board()
                if board.has_won(symbol):
                    print(f"Player {symbol} has won!")
                    return
                if board.is_full():
                    print("It's a tie! Try again.")
                    return
                symbol = 'O' if symbol == 'X' else 'X'
            except Exception as e:
                print(e)

if __name__ == "__main__":
    board = Board()
    game = Game(board)
    game.play()
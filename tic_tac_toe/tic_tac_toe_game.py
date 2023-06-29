"""
Create a playable Tic Tac Toe game

two players, x and o
x goes first
x and o take turns

winner is first player to get three in a row, a column, diagonal, or anti-diagonal

get move, check if valid, check if move wins, repeat until winner or board full

"""

BOARD_SIZE = 3
FIRST_PLAYER = "X"


class TicTacToeGame:
    def __init__(self):
        self.player = FIRST_PLAYER
        self.winner = ""
        self.move_count = 0
        self.board = self.create_board()

    def create_board(self) -> list[list[str]]:
        """Create a new board"""

        return [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if move is valid"""
        # TODO: check if we have a winner?
        if self.board[row][col]:
            return False
        self.move_count += 1
        return True

    def is_board_full(self) -> bool:
        """Check if board is full"""

        return self.move_count == BOARD_SIZE * BOARD_SIZE

    def check_row(self, player: str, row: int) -> bool:
        """Check for winner in row"""

        for col in range(BOARD_SIZE):
            if self.board[row][col] != player:
                return False
        return True

    def check_column(self, player: str, col: int) -> bool:
        """Check for winner in column"""

        for row in range(BOARD_SIZE):
            if self.board[row][col] != player:
                return False
        return True

    def check_diagonal(self, player: str) -> bool:
        """Check for winner in diagonal"""

        for row in range(BOARD_SIZE):
            if self.board[row][row] != player:
                return False
        return True

    def check_anti_diagonal(self, player: str) -> bool:
        """Check for winner in anti-diagonal"""

        for row in range(BOARD_SIZE):
            col = BOARD_SIZE - row - 1
            if self.board[row][col] != player:
                return False
        return True

    def has_winner(self, player: str, row: int, col: int) -> bool:
        """Determine if current move is a winning move"""

        return any(
            [
                self.check_row(player, row),
                self.check_column(player, col),
                self.check_diagonal(player),
                self.check_anti_diagonal(player),
            ]
        )

    def update_board(self, row: int, col: int) -> None:
        """Update board with player's move"""

        self.board[row][col] = self.player

    def switch_players(self) -> None:
        self.player = "X" if self.player == "O" else "O"

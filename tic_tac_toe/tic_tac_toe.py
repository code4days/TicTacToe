"""
Create a playable Tic Tac Toe game

two players, x and o
x goes first
x and o take turns

winner is first player to get three in a row, a column, diagonal, or anti-diagonal

get move, check if valid, check if move wins, repeat until winner or board full

"""
SIZE = 3
FIRST_PLAYER = "x"

#


def create_board() -> list[list[str]]:
    """Create a new board"""

    return [["" for _ in range(SIZE)] for _ in range(SIZE)]


def get_move() -> tuple[int, int]:
    """Get a move from the user"""

    # get move from user
    row, col = input("Enter row and column separated by space: ").split()
    return (int(row), int(col))


def is_valid_move(board: list[list[str]], row: int, col: int) -> bool:
    """Check if move is valid"""

    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return False
    if board[row][col]:
        return False
    return True


def is_board_full(move_count: int) -> bool:
    """Check if board is full"""

    if move_count == SIZE * SIZE:
        return True
    return False


def check_row(board: list[list[str]], player: str, row: int) -> bool:
    """Check for winner in row"""

    for col in range(SIZE):
        if board[row][col] != player:
            return False
    return True


def check_column(board: list[list[str]], player: str, col: int) -> bool:
    """Check for winner in column"""

    for row in range(SIZE):
        if board[row][col] != player:
            return False
    return True


def check_diagonal(board: list[list[str]], player: str) -> bool:
    """Check for winner in diagonal"""

    for row in range(SIZE):
        if board[row][row] != player:
            return False
    return True


def check_anti_diagonal(board: list[list[str]], player: str) -> bool:
    """Check for winner in anti-diagonal"""

    for row in range(SIZE):
        col = SIZE - row - 1
        if board[row][col] != player:
            return False
    return True


def check_winner(board: list[list[str]], player: str, row: int, col: int) -> bool:
    """Determine if current move is a winning move"""

    return any(
        [
            check_row(board, player, row),
            check_column(board, player, col),
            check_diagonal(board, player),
            check_anti_diagonal(board, player),
        ]
    )


def update_board(board: list[list[str]], player: str, row: int, col: int) -> None:
    """Update board with player's move"""

    board[row][col] = player


def print_board(board: list[list[str]]) -> None:
    """Print the board"""

    for row in board:
        print(row)


def play_game() -> None:
    """Play a game of Tic Tac Toe"""

    # create board
    board = create_board()
    # set first player to x
    player = FIRST_PLAYER
    winner = ""
    move_count = 0

    # while no winner and board not full
    while True:
        # get move
        row, col = get_move()

        # check if move is valid
        if not is_valid_move(board, row, col):
            # tell user move is not valid
            print("Invalid move")
            continue

        move_count += 1
        update_board(board, player, row, col)

        if check_winner(board, player, row, col):
            winner = player
            break

        if is_board_full(move_count):
            break

        # switch players
        player = "x" if player == "o" else "o"

        print_board(board)

    # print winner
    if winner:
        print(f"{winner} wins!")
    else:
        print("Tie game")


if __name__ == "__main__":
    play_game()

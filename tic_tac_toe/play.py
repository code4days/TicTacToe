from typing import Final

from textual import on
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Footer, Header, Label

from tic_tac_toe.tic_tac_toe_game import TicTacToeGame

"""
This is a simple Tic Tac Toe game with a Textual interface.
It is a work in progress.

TODO:
- add the ability to restart the game
"""


class GameCell(Button):
    # TODO: consider making this a module-level function.
    @staticmethod
    def at(row: int, col: int) -> str:
        """ID of the cell at given location"""

        return f"cell-{row}-{col}"

    def __init__(self, row: int, col: int) -> None:
        super().__init__("", id=self.at(row, col))
        self.row = row
        self.col = col


class GameGrid(Widget):
    def compose(self) -> ComposeResult:
        for row in range(TicTacToeApp.SIZE):
            for col in range(TicTacToeApp.SIZE):
                yield GameCell(row, col)


class TicTacToeApp(App):
    """Tic Tac Toe game with Textual interface"""

    CSS_PATH = "tictactoe.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    TITLE = "Play Tic Tac Toe"

    SIZE: Final = 3

    def __init__(self) -> None:
        super().__init__()
        self.game = TicTacToeGame()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header()
        yield Footer()
        # yield Label("Play Tic Tac Toe")
        yield GameGrid()
        yield Label(id="winner-label")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def _update_button(self, button: GameCell, player: str):
        """Update button with player's symbol"""

        button.label = player
        button.disabled = True
        button.classes = player

    def _update_winner_label(self, msg: str) -> None:
        """Update winner label with message"""

        winner_label = self.query_one("#winner-label", Label)
        winner_label.update(msg)
        winner_label.visible = True

    def _game_playable(self, playable: bool) -> None:
        """Update game playability"""

        self.query_one(GameGrid).disabled = not playable

    @on(Button.Pressed)
    def handle_button_pressed(self, message: Button.Pressed):
        """Handle a button pressed event"""

        row, col = message.button.row, message.button.col

        if self.game.is_valid_move(row, col):
            self._update_button(message.button, self.game.player)
            self.game.update_board(row, col)

            if self.game.has_winner(player=self.game.player, row=row, col=col):
                msg = f"Player {self.game.player} wins!"
                self._game_playable(False)
                self._update_winner_label(msg)
                return

            if self.game.is_board_full():
                msg = "Game Tied"
                self._game_playable(False)
                self._update_winner_label(msg)
                return
        self.game.switch_players()


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()

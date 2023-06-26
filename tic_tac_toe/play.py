from typing import Final

from textual import on
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Footer, Header, Label


# q: are you familiar with textual and how it works?



"""
This is a simple Tic Tac Toe game with a Textual interface.
It is a work in progress.

TODO:
Write code to play game.
Write code to determine winner.
Write code to reset game.
Write code to play again.
Write code to play against computer.
Write code to play against another player.
Handle UI events.
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

    SIZE: Final = 3

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""

        yield Header()
        yield Footer()
        yield Label("Play Tic Tac Toe")
        yield GameGrid()
        yield Label("Winner:")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    
    @on(Button.Pressed)
    def handle_button_pressed(self, message: Button.Pressed):
        """Handle a button pressed event"""
        
        print(f"Button {message.button.id} pressed")
        message.button.label = "X"
        message.button.disabled = True
        message.button.classes = "x"



    


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()

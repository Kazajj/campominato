# minesweeper.py
from campominato.controller.controller import Controller
from campominato.graphic.screen_view import ScreenView
from campominato.model.model_game import ModelGame


class MineSweeper:
    @staticmethod
    def main():
        x, y, bombs = 10, 10, 10

        # Initialize components
        model_game = ModelGame()
        controller = Controller(model_game)
        listener = ScreenView(controller)

        # Link the controller with the listener
        controller.set_listener(listener)

        # Set up the game grid
        controller.choose_grid_size(x, y, bombs)


if __name__ == "__main__":
    MineSweeper.main()

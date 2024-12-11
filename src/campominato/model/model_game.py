from enum import Enum

from campominato.object.box import Box
from campominato.object.game_state import GameState


class ModelGame:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bombs = 0
        self.state = GameState.WAITING
        self.boxes = []
        self.status_bombs = 0

    def generate_boxes(self):
        """Generates a grid of Box objects."""
        self.boxes = [[Box(i, j) for j in range(self.y)] for i in range(self.x)]

    def get_box(self, x, y):
        """Returns the Box at position (x, y)."""
        return self.boxes[x][y]

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_bombs(self):
        return self.bombs

    def set_bombs(self, bombs):
        self.bombs = bombs

    def get_boxes(self):
        return self.boxes

    def set_boxes(self, boxes):
        self.boxes = boxes

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def is_win(self):
        return self.state == GameState.WIN

    def is_started(self):
        return self.state == GameState.STARTED

    def is_not_started(self):
        return not self.is_started()

    def is_waiting(self):
        return self.state == GameState.WAITING

    def is_game_over(self):
        return self.state == GameState.GAMEOVER

    def increase_bombs_status(self):
        self.status_bombs += 1

    def decrease_bombs_status(self):
        self.status_bombs -= 1

    def get_status_bombs(self):
        return self.status_bombs

    def set_status_bombs(self, bombs):
        self.status_bombs = bombs

import random
from collections import namedtuple

from campominato.object.game_state import GameState


class Controller:
    def __init__(self, model_game):
        self.model_game = model_game
        self.listener = None

    def choose_grid_size(self, x, y, bombs):
        self.model_game.set_x(x)
        self.model_game.set_y(y)
        self.model_game.set_bombs(bombs)
        self.model_game.set_status_bombs(bombs)
        self.model_game.generate_boxes()
        if self.listener:
            self.listener.generate_game_panel()

    def on_left_click(self, x, y):
        if self.model_game.is_win() or self.model_game.is_game_over():
            return

        if self.model_game.is_not_started() and not self.get_box(x, y).is_flag():
            self.generate_bombs(x, y)
            return

        box = self.get_box(x, y)
        if box.is_checked() or box.is_flag():
            return

        if box.is_bomb():
            self.model_game.set_state(GameState.GAMEOVER)
            if self.listener:
                self.listener.update_graphic()
            return
        else:
            self.check_boxes(x, y)
            if self.listener:
                self.listener.update_graphic()
            self.check_win()
            if self.listener:
                self.listener.update_graphic()

    def generate_bombs(self, x, y):
        first_click = (x, y)
        for _ in range(self.model_game.get_bombs()):
            while True:
                x_bomb = random.randint(0, self.get_x() - 1)
                y_bomb = random.randint(0, self.get_y() - 1)
                random_coordinate_bomb = (x_bomb, y_bomb)
                if self.box_not_available(first_click, random_coordinate_bomb):
                    continue
                if self.get_box(x_bomb, y_bomb).is_bomb():
                    continue
                self.get_box(x_bomb, y_bomb).set_bomb(True)
                break

        self.model_game.set_state(GameState.STARTED)
        self.set_box_values()
        self.clear_boxes(*first_click)
        if self.listener:
            self.listener.update_graphic()

    def box_available(self, first_click, random_coordinate_bomb):
        x_first_click, y_first_click = first_click
        for i in range(-1, 2):
            for j in range(-1, 2):
                if random_coordinate_bomb == (x_first_click + i, y_first_click + j):
                    return False
        return True

    def box_not_available(self, first_click, random_coordinate_bomb):
        return not self.box_available(first_click, random_coordinate_bomb)

    def clear_boxes(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.check_boxes(x + i, y + j)

    def set_box_values(self):
        for i in range(self.get_x()):
            for j in range(self.get_y()):
                if self.get_box(i, j).is_bomb():
                    self.double_for(self.increase_box_value, i, j)

    def increase_box_value(self, x, y):
        if not self.is_array_index_out_of_bounds(x, y):
            self.get_box(x, y).increase_value()

    def double_for(self, biconsumer, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                biconsumer(x + i, y + j)

    def check_boxes(self, x, y):
        if self.is_array_index_out_of_bounds(x, y):
            return
        box = self.get_box(x, y)
        if not box.is_checked() and not box.is_bomb() and not box.is_flag():
            box.set_checked(True)
            if box.get_value() == 0:
                self.clear_boxes(x, y)

    def check_win(self):
        counter = 0
        for i in range(self.get_x()):
            for j in range(self.get_y()):
                if not self.get_box(i, j).is_bomb() and self.get_box(i, j).is_checked():
                    counter += 1
        if counter == self.get_x() * self.get_y() - self.model_game.get_bombs():
            self.model_game.set_state(GameState.WIN)

    def is_array_index_out_of_bounds(self, x, y):
        return x < 0 or x >= self.get_x() or y < 0 or y >= self.get_y()

    def is_not_array_index_out_of_bounds(self, x, y):
        return not self.is_array_index_out_of_bounds(x, y)

    def on_right_click(self, x, y):
        if self.get_box(x, y).is_checked():
            return
        box = self.get_box(x, y)
        if box.is_flag():
            box.set_flag(False)
            self.model_game.increase_bombs_status()
        else:
            box.set_flag(True)
            self.model_game.decrease_bombs_status()

    def set_listener(self, listener):
        self.listener = listener

    def get_box(self, x, y):
        return self.model_game.get_box(x, y)

    def get_x(self):
        return self.model_game.get_x()

    def get_y(self):
        return self.model_game.get_y()

    def is_win(self):
        return self.model_game.is_win()

    def is_game_over(self):
        return self.model_game.is_game_over()

    def get_status_bombs(self):
        return self.model_game.get_status_bombs()

    def get_bombs(self):
        return self.model_game.get_bombs()

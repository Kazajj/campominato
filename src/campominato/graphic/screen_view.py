import tkinter as tk
from tkinter import messagebox

from campominato.graphic.game_button import GameButton


class ScreenView:
    STATUS_BAR = 150
    REMAINING_BOMBS = "Remaining bombs: "

    def __init__(self, controller):
        self.controller = controller
        self.frame = tk.Tk()
        self.frame.title("Minesweeper")
        self.panel = tk.Frame(self.frame)
        self.status = None
        self.bombs = None
        self.buttons = []

    def generate_game_panel(self):
        """
        Initializes the main game panel with buttons and status bars.
        """
        grid_width = 50 * self.controller.get_x() + self.STATUS_BAR
        grid_height = 50 * self.controller.get_y()

        self.panel.config(width=grid_width, height=grid_height)
        self.panel.grid(row=0, column=0)

        self.generate_boxes()
        self.generate_status()

        self.frame.mainloop()

    def generate_boxes(self):
        """
        Generates the Minesweeper grid as buttons.
        """
        rows, cols = self.controller.get_x(), self.controller.get_y()
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                btn = GameButton(self.panel)
                btn.set_coordinate_x_and_y(i, j)
                btn.grid(row=j, column=i)  # Note: Tkinter uses (row, column)
                btn.bind("<Button-1>", self.on_left_click)
                btn.bind("<Button-3>", self.on_right_click)
                self.buttons[i][j] = btn

    def generate_status(self):
        """
        Adds status bars for remaining bombs and total bombs.
        """
        self.status = tk.Label(self.frame, text=f"{self.REMAINING_BOMBS}{self.controller.get_bombs()}")
        self.status.grid(row=0, column=1, sticky="w")

        self.bombs = tk.Label(self.frame, text=f"Total bombs: {self.controller.get_bombs()}")
        self.bombs.grid(row=1, column=1, sticky="w")

    def update_graphic(self):
        """
        Updates the graphical interface based on the current game state.
        """
        if self.controller.is_game_over() or self.controller.is_win():
            self.gameover_graphics()
            return

        for i in range(self.controller.get_x()):
            for j in range(self.controller.get_y()):
                box = self.controller.get_box(i, j)
                btn = self.buttons[i][j]

                if box.is_flag():
                    btn.config(bg="cyan")
                else:
                    btn.config(bg="light gray")
                    self.is_checked(i, j)

        self.status.config(text=f"{self.REMAINING_BOMBS}{self.controller.get_status_bombs()}")

    def gameover_graphics(self):
        """
        Displays the game over screen.
        """
        for i in range(self.controller.get_x()):
            for j in range(self.controller.get_y()):
                btn = self.buttons[i][j]
                btn.config(state=tk.DISABLED)

                if self.controller.get_box(i, j).is_bomb():
                    color = "green" if self.controller.is_win() else "red"
                    btn.config(bg=color)

    def is_checked(self, i, j):
        """
        Marks the button as checked, updating its state and appearance.
        """
        box = self.controller.get_box(i, j)
        btn = self.buttons[i][j]

        if box.is_checked():
            btn.config(state=tk.DISABLED, bg="white")
            if box.value != 0:
                btn.config(text=str(box.value))

    def on_left_click(self, event):
        """
        Handles left mouse click events.
        """
        btn = event.widget
        x, y = btn.get_coordinate_x(), btn.get_coordinate_y()
        self.controller.on_left_click(x, y)
        self.update_graphic()

    def on_right_click(self, event):
        """
        Handles right mouse click events.
        """
        btn = event.widget
        x, y = btn.get_coordinate_x(), btn.get_coordinate_y()
        self.controller.on_right_click(x, y)
        self.update_graphic()

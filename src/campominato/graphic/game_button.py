import tkinter as tk


class GameButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        """
        Initialize the GameButton, setting its size and default background color.
        """
        super().__init__(master, **kwargs)
        self.coordinataX = 0
        self.coordinataY = 0

        # Set default properties
        self.config(width=5, height=2, bg="light gray")

    def get_coordinate_x(self):
        """
        Get the X coordinate of the button.
        """
        return self.coordinataX

    def get_coordinate_y(self):
        """
        Get the Y coordinate of the button.
        """
        return self.coordinataY

    def set_coordinate_x_and_y(self, coordinataX, coordinataY):
        """
        Set the X and Y coordinates of the button.
        """
        self.coordinataX = coordinataX
        self.coordinataY = coordinataY

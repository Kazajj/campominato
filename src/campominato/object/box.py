class Box:
    def __init__(self, x, y):
        self.bomb = False
        self.checked = False
        self.flag = False
        self.value = 0
        self.x = x
        self.y = y

    def increase_value(self):
        """
        Increase the value of the box (typically used when counting adjacent bombs).
        """
        self.value += 1

    def is_bomb(self):
        """
        Returns True if the box is a bomb.
        """
        return self.bomb

    def is_not_bomb(self):
        """
        Returns True if the box is not a bomb.
        """
        return not self.is_bomb()

    def set_bomb(self, bomb):
        """
        Sets whether this box is a bomb.
        """
        self.bomb = bomb

    def get_value(self):
        """
        Returns the value of the box (how many bombs are adjacent to it).
        """
        return self.value

    def set_value(self, value):
        """
        Sets the value of the box.
        """
        self.value = value

    def get_x(self):
        """
        Returns the x coordinate of the box.
        """
        return self.x

    def set_x(self, x):
        """
        Sets the x coordinate of the box.
        """
        self.x = x

    def get_y(self):
        """
        Returns the y coordinate of the box.
        """
        return self.y

    def set_y(self, y):
        """
        Sets the y coordinate of the box.
        """
        self.y = y

    def is_checked(self):
        """
        Returns True if the box is checked.
        """
        return self.checked

    def is_not_checked(self):
        """
        Returns True if the box is not checked.
        """
        return not self.is_checked()

    def set_checked(self, checked):
        """
        Sets the checked state of the box.
        """
        self.checked = checked

    def is_flag(self):
        """
        Returns True if the box is flagged.
        """
        return self.flag

    def is_not_flag(self):
        """
        Returns True if the box is not flagged.
        """
        return not self.is_flag()

    def set_flag(self, flag):
        """
        Sets the flag state of the box.
        """
        self.flag = flag

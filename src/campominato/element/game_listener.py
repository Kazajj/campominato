from abc import ABC, abstractmethod


class GameListener(ABC):

    @abstractmethod
    def generate_game_panel(self):
        """Method to generate the game panel."""
        pass

    @abstractmethod
    def update_graphic(self):
        """Method to update the game graphic."""
        pass

    @abstractmethod
    def on_time_expired(self):
        """Method to handle when the time expires."""
        pass

from GameFrame import Level
from Objects.Win import Win

class WinScreen(Level):
    """
    Win screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add win object
        self.add_room_object(Win(self, 0, 0))

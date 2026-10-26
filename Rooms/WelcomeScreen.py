from GameFrame import Level
from Objects.Title import Title

class WelcomeScreen(Level):
    """
    Initial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add title object
        self.add_room_object(Title(self, 240, 200))
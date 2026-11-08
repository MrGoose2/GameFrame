from GameFrame import Level

class WinScreen(Level):
    """
    Win screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("Win.png")
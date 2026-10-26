from GameFrame import Level
from Objects import Deny
from Objects.Accept import Accept

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add accept object
        self.add_room_object(Accept(self, 440, 600))

        # add deny object
        self.add_room_object(Deny(self, 10, 600))

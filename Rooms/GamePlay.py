from GameFrame import Level
from Objects import Deny
from Objects.Accept import Accept
from Objects.GoodTest import GoodTest

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add accept object
        self.add_room_object(Accept(self, 440, 650))

        # add deny object
        self.add_room_object(Deny(self, 10, 650))

        #add good test object
        self.add_room_object(GoodTest(self, 5, 10))

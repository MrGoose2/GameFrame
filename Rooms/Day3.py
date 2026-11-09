import random
from GameFrame import Level
import Objects
from Objects.Deny import Deny
from Objects.Accept import Accept
from Objects.Legit_6 import Legit6
from Objects.Legit_7 import Legit7
from Objects.Phishing_3 import Phish3
from Objects.Phishing_4 import Phish4
from Objects.Phishing_5 import Phish5

class Day3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # Pool of email classes
        self.email_pool = [Legit6, Phish3, Legit7, Phish4, Phish5]
        self.current_email = None

        # Add buttons to the room
        self.add_room_object(Accept(self, 440, 650))
        self.add_room_object(Deny(self, 10, 650))

        # Load the first email
        self.spawn_next_email()

    def spawn_next_email(self):
        # Delete old email if it exists
        if self.current_email:
            self.delete_object(self.current_email)
            self.current_email = None

        # Spawn next or trigger win screen
        if len(self.email_pool) > 0:
            SelectedEmailClass = self.email_pool.pop(random.randrange(len(self.email_pool)))
            self.current_email = SelectedEmailClass(self, 5, 10)
            self.add_room_object(self.current_email)
        else:
            self.running = False

        # load sound files
        self.incorrect_sound = self.load_sound("wrong.mp3")
        self.correct_sound = self.load_sound("correct.mp3")
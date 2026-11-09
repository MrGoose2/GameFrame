import random
from GameFrame import Level
from Objects.Deny import Deny
from Objects.Accept import Accept
from Objects.Legit_3 import Legit3
from Objects.Legit_4 import Legit4
from Objects.Legit_5 import Legit5
from Objects.Phishing_2 import Phish2

class Day2(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # Pool of email classes
        self.email_pool = [Legit3, Phish2, Legit4, Legit5]
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
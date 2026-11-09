import pygame
from GameFrame import RoomObject

class Accept(RoomObject):
    """
    The object for displaying the Accept button
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # image
        image = self.load_image("Accept.png")
        self.set_image(image, 243, 129)
        
        # anti spam cooldown
        self.key_cooldown = 0

    def update(self):
        if self.key_cooldown > 0:
            self.key_cooldown -= 1

        # check if key pressed
        keys = pygame.key.get_pressed()
        
        # register key 2
        if keys[pygame.K_2] and self.key_cooldown == 0:
            self.key_cooldown = 15
            
            current = self.room.current_email
            if current is not None:
                if current.is_phishing == False:
                    self.room.spawn_next_email()
                    self.room.correct_sound.play()
                else:
                    self.room.incorrect_sound.play()
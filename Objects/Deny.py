import pygame
from GameFrame import RoomObject

class Deny(RoomObject):
    """
    The object for displaying the Deny button
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # image
        image = self.load_image("Deny.png")
        self.set_image(image, 243, 129)
        
        # anti spam cooldown
        self.key_cooldown = 0

    def update(self):
        if self.key_cooldown > 0:
            self.key_cooldown -= 1

        # check if key pressed
        keys = pygame.key.get_pressed()
        
        # register key 1
        if keys[pygame.K_1] and self.key_cooldown == 0:
            self.key_cooldown = 15
            
            current = self.room.current_email
            if current is not None:
                if current.is_phishing == True:
                    self.room.spawn_next_email()
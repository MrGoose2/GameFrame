from GameFrame import RoomObject
import pygame

class Win(RoomObject):
    """
    The object for displaying the win
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Win.png")
        self.set_image(image,1500,914)
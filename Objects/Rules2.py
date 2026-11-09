from GameFrame import RoomObject
import pygame

class Rules2(RoomObject):
    """
    The object for displaying the rules for Day 2
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Rules2.png")
        self.set_image(image,226,436)
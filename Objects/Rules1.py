from GameFrame import RoomObject
import pygame

class Rules1(RoomObject):
    """
    The object for displaying the rules for Day 1
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Rules1.png")
        self.set_image(image,226,436)
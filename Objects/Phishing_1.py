from GameFrame import RoomObject

class Phish1(RoomObject):
    """
    The object for displaying the bad email
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.is_phishing = True

        # set image
        image = self.load_image("Phish 1.png")
        self.set_image(image,784,1123)
from GameFrame import RoomObject

class Phish4(RoomObject):
    """
    The object for displaying the 4th bad email
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.is_phishing = True

        # set image
        image = self.load_image("Phish 4.png")
        self.set_image(image,784,1123)
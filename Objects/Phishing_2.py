from GameFrame import RoomObject

class Phish2(RoomObject):
    """
    The object for displaying the 2nd bad email
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.is_phishing = True

        # set image
        image = self.load_image("Phish 2.png")
        self.set_image(image,784,1123)
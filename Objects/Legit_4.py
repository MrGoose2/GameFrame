from GameFrame import RoomObject

class Legit4(RoomObject):
    """
    The object for displaying the 4th good email
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.is_phishing = False

        # set image
        image = self.load_image("Legit 4.png")
        self.set_image(image,784,1123)
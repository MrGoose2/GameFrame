from GameFrame import RoomObject

class GoodTest(RoomObject):
    """
    The object for displaying the good email
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.is_phishing = False

        # set image
        image = self.load_image("GoodTest.png")
        self.set_image(image,784,1123)
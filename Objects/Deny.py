from GameFrame import RoomObject

class Deny(RoomObject):
    """
    The object for displaying the deny button
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Deny.png")
        self.set_image(image,243,129)
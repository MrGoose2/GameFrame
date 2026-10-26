from GameFrame import RoomObject

class Accept(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Accept.png")
        self.set_image(image,243,129)
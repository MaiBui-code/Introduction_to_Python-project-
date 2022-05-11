class SampleGridSquare( object ):
    """A simple class to represent a square in a grid and maintains
    its corresponding GUI element and some text."""

    def __init__(self, text, guiElement):
        """ Construct a new instance of a square with the given text and established GUI 
        element (expected to be a Tkinter label). """

        self.__text = text # initialize instance property to maintain the text
        self.__guiElement = guiElement # initialize instance property to track the GUI

    def revealText (self):
        """Update the GUI element to show the text for this square and change 
        the background color to white"""
        backgroundColor = "PeachPuff3"
        self.__guiElement.configure (bg=backgroundColor)
        #text = str(self.__text)
    def changeColor(self, color):
        self.__guiElement.configure (bg = color)
    def takeColor(self):
        return self.__guiElement["bg"]
        
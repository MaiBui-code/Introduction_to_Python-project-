import tkinter # the Tkinter module gives us access to GUI elements

#this is how we import a class from another file in the same directory
from SampleGridSquare import SampleGridSquare

class SampleGridGUI( object):
    """This is a sample GUI that creates a window full of squares that can be clicked."""
    def __init__ (self, numRows, numCols):
        # the squares instance property will be a 2D list that
        #stores each square in the corresponding
        #row and column that it appears in the GUI
        self.__squares = []

        #store the rows sand columns in instance properties
        self.__numRows = numRows
        self.__numCols = numCols

        #initialize the board with the squares and corresponding GUI elements
        self.initBoard()
    def initBoard (self):
        """Initilize the GUI elements and the squares instance property."""

        #this is the initialization code for Tkinter to create the window that will pop up
        window = tkinter.Tk()

        #this sets the title that shows at the top of the window
        window.title ("Sample Grid GUI")

        #sets width and height
        window.geometry("475x540")

        #check out this site for string literals that TKinter can interpret as colors
        squareColor1 = "DarkOrange1"
        squareColor2 = "DarkOrchid4"
        squareColor3 = ""
        squareColor4 = ""
        #initialize the rows
        for rowIndex in range (self.__numRows):

            #create a list for this row
            self.__squares.append([])

            #initialize the squares for this row (one for each column index)
            for colIndex in range(self.__numCols):

                #alternate background colors 
                if (rowIndex + colIndex) % 2 == 0:
                    squareColor = squareColor1
                else:
                    squareColor = squareColor2
                
                # create a Tkinter GUI label, specifying the background color, text, width and height
                label = tkinter.Label(window, bg=squareColor, text = " ", width=3, height=2)
                #when the label is clicked, we want to invoke the 
                #instance method handleClick and pass the row and column indices 
                #the following code lets us do this
                def handler (event, row=rowIndex, col=colIndex):
                    #this will send the corresponding info to the instance method
                    return self.handleClick(event, row, col)

                #now that we've made this "handler" function, we want it to be "bound"
                #to the label GUI interface so that clicking the label will result in 
                #the handleClick method being ivnoked 
                label.bind('<Button>', handler)

                #add it to the GUI at the correct row and index
                label.grid(row = rowIndex, column = colIndex)

                #change the color of the label
                #squareColor1 = "DarkSeaGreen4"
                label = tkinter.Label(window, bg=squareColor2, text = "", width=3, height=2)

                #make a new SampleGridSquare instance with some text for later and the label
                square = SampleGridSquare( "a", label)
                
                #keep track of it in the squares instance property
                self.__squares[rowIndex].append(square)
            window.mainloop()
    def handleClick(self, event, rowIndex, colIndex):
            """This instance method should be invoked in response to a square being clicked."""

            print( f"The square at {rowIndex}, {colIndex} was clicked.")
            #make sure this is a valid rowIndex and colIndex
            if rowIndex >= 0 and rowIndex < len(self.__squares) and colIndex >= 0 and colIndex < len(self.__squares[0]):
                clickedSquare = self.__squares[rowIndex][colIndex]
            else:
                clickedSquare = None

            #as long as we actually found the corresponding SampleGridSquare instance 
            if clickedSquare != None:
                #have it reveal its text
                clickedSquare.revealText()

def main():
    # create a SampleGridGUI instance, which should pop up a window
    # try with 14x14 grid
    sampleGUI = SampleGridGUI(14,14)

#test it out with the main function
main()             
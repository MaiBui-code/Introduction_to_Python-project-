import tkinter # the Tkinter module gives us access to GUI elements
import random
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
        window.geometry("700x600")

        #check out this site for string literals that TKinter can interpret as colors
        #set the 5 specific color
        squareColorList = ["DarkOrange1", "DarkOrchid4", "RosyBrown2","blue2","aquamarine2"]

        #initialize the rows
        for rowIndex in range (self.__numRows):

            #create a list for this row
            #self.__squares.append([])
            row = []

            #initialize the squares for this row (one for each column index)
            for colIndex in range(self.__numCols):
                
                #alternate background colors 
                # random the color of the square 
                color = random.randint(0,4)
                squareColor = squareColorList[color]
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
                #label = tkinter.Label(window, bg=squareColor, text = "", width=3, height=2)

                #make a new SampleGridSquare instance with some text for later and the label
                square = SampleGridSquare( " ", label)
                
                #keep track of it in the squares instance property
                row.append(square)
            
            #add the row to the squares
            
            self.__squares.append(row)

        window.mainloop()
    def handleClick(self, event, rowIndex, colIndex):
            """This instance method should be invoked in response to a square being clicked."""

            print( f"The square at {rowIndex}, {colIndex} was clicked.")
            #make sure this is a valid rowIndex and colIndex
            if rowIndex >= 0 and rowIndex < len(self.__squares) and colIndex >= 0 and colIndex < len(self.__squares[0]):
                clickedSquare = self.__squares[rowIndex][colIndex]
            else:
                clickedSquare = None
            #change the left corner square color into the color we click on
            #self.__squares[0][0]

            #as long as we actually found the corresponding SampleGridSquare instance 
            if clickedSquare != None:
                #have it reveal its text
                #clickedSquare.revealText()
                #take the color of the clicked square 
                color = clickedSquare.takeColor()

                #attach the color from the clicked square to the top left corner square                
                self.__squares[0][0].changeColor(color)
                
                #change the color of the surround squares into the clicked squares
                #to do so, step 1: store all the previous checked squares into a list
                checkedList = []
                checkColorList = []
                #check the color of the squares around it
                for r in range(1,self.__numRows):
                    checkSquares1 = self.__squares[r][0]
                    checkColor = checkSquares1.takeColor()
                    #create a list containing color of each square in the same column
                    checkColorList.append(checkColor)
                    #add the checkSquare to the checked list 
                    checkedList.append(checkSquares1)
                #create a dictionary with the square and its color
                dictColor = {}
                for checkColor2 in checkColorList:
                    for nameSquare in checkedList:
                        dictColor[checkColor2] = nameSquare
                        checkedList.remove(nameSquare)
                        break
                #keep track of the checkColor
                #start it with the first square
                
                b = 0
                #create a list of changed Color list
                changedColorList = [self.__squares[0][0]]
                #if the color of the checked square is the same with the clicked square
                #for r in range(1,self.__numRows):
                while checkColorList[b] == color:
                    #change the color of the checked squares into the color of the clicked square
                    #for checked in checkedList:
                    #    checked.changeColor(color)
                    #add it to the changedColorList 
                    changedColorList.append(dictColor[checkColorList[b]])
                    for changeColorSquare in changedColorList:
                        changeColorSquare.changeColor(color)
                    b = b + 1

                
def main():
    # create a SampleGridGUI instance, which should pop up a window
    # try with 14x14 grid
    sampleGUI = SampleGridGUI(18,18)

#test it out with the main function
main()             
import tkinter

class ClickCounter (object):
    def __init__(self):
        self._clickCount = 0 # initialize an instance property to count the number of the clicks
        self.initGUI() # initialize the GUI

    def initGUI(self):
        """A basic GUI to get us started."""
        # this is the initialization code for Tkinter to create the window that will pop up
        window = tkinter.Tk()

        #this sets the title that shows at the top of the window
        window.title("Get started")

        #this sets the width and the height of the window (in pixels)
        window.geometry("200x100")
        
        #create a Tkinter GUI label, specifying sone text to display
        label = tkinter.Label(window, text = "Hello, Word!")

        #we want to know when the label is clicked
        #since this is now within a class definition, we have to do a little more 
        #to notify ourselves of a click using an instance method
        def handler (event):
            return self.handleClick(event)
        label.bind( '<Button>', handler)

        #add label to the grid layout
        label.grid(row = 0, column = 0)

        #ask the window to launch
        window.mainloop()
    def handleClick(self,event):
        """ An instance property that should be involked in response to a label being clicked."""
        self._clickCount += 1 # increment the click count
        print (f"The label was clicked a total of {self._clickCount} times!")

#test it out
clickCounter = ClickCounter()
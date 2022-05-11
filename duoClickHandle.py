import tkinter

class DuoClickCounter(object):
    def __init__ (self):
        self.__clickCount1 = 0 #initialize an instance property to count the number of clicks
        self.__clickCount2 = 0 
        self.initGUI() # initialize the GUI
    def initGUI(self):
        #set up the window
        window = tkinter.Tk()
        
        #set up the title
        window.title("Get started")

        #set up the width and the height of the window
        window.geometry("600x600")

        #create the 1st Tkinter GUI label 
        label1 = tkinter.Label(window, text = "1")

        #we want to know when the label is clicked
        #and we want to send some information along
        #the following code lets us to do this --
        def handler (event, number = 1):
            return self.handleClick (event, number)
        label1.bind('<Button>', handler)

        #add it to the GUI
        label1.grid(row = 0, column = 0)

        #create the 2nd label
        label2 = tkinter.Label(window, text = "2")

        #we want to know when the 2nd label is clicked
        def handler (event, number = 2):
            return self.handleClick(event, number)
        label2.bind('<Button>', handler)

        #add the 2nd label to the GUI
        label2.grid(row =1, column = 0)

        #ask the window to launch
        window.mainloop()
    def handleClick(self, event, num):
        """An instance property that should be invoked in response to a label being clicked."""
        
        if num == 1: #label1 was clicked
            self.__clickCount1 += 1
            print (f"The label {num} was clicked a total of {self.__clickCount1} times!")
        elif num == 2: #label2 was clicked
            self.__clickCount2 += 1
            print (f"The label {num} was clicked a total of {self.__clickCount2} times!")

#test it out
clickCounter = DuoClickCounter()
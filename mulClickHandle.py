import tkinter

class MulClickHandle(object):
    def __init__(self):
        self.__clickCount = [0] * 25; 
        self.initGUI() # initialize the GUI
    def initGUI(self):
        """A basic GUI to get us started."""

        #set up the window
        window = tkinter.Tk()

        #set up the title 
        window.title("Get started!")

        #set up the height and the width
        window.geometry("600x300")
        
        #create the labelList
        labelList = []
        """figure out another way to set up 25 variables without making it by hand"""
        for i in range (0,25):
            labelList.append(tkinter.Label(window, text = str(i + 1)))
            def handler (event, number = i + 1):
                return self.handleClick(event, number)
            labelList[i].bind('<Button>', handler)

            labelList[i].grid(row = i, column = 0)
        
        #ask the window to launch
        window.mainloop()
    def handleClick(self,event, num):
        for i in range (0,25):
            if num == i + 1:
                self.__clickCount[i] += 1 #increment the click count
                print (f"The label {num} was clicked a total of {self.__clickCount[i]} times!")
            
#test it out
clickCounter = MulClickHandle()
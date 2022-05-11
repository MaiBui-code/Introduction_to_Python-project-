import tkinter

def helloTkinter():
    #create the window 
    window = tkinter.Tk()
    #set the title at the top of the window
    window.title("Get started")
    #set the width and height 
    window.geometry("200x200")
    #create a Tkinter GUI label, specifying some text to display
    #create a variable to label from 1-15
    num = 1
    for r in range (0,3):
        for c in range (0,5):
            label = tkinter.Label(window, text = num)
            # when the label is clicked, we want be able to handle this
            # to do so, we can "bind" the click (making this label "act" like a button)
            # to a particular function
            # NOTICE that we are NOT invoking the function, but actually passing the name itself
            label.bind('<Button>', handleClick)
            #add it to the GUI using a grid layout
            label.grid(row = r, column = c)
            num = num + 1
    #add the second text
    #label2 = tkinter.Label(window, text = "Hello, MHC!")
    #add it under the previous text
    #label2.grid(row = 1, column = 0)
    #ask the window to launch
    window.mainloop()

def handleClick(event):
    #A function that should be invoked in response to a label being clicked
    print ("The label was clicked!")

#test it
helloTkinter()
#input = nothing
#output = numberOfSticks
def setInitialSticks ():

    print ("Welcome to the Game of Sticks.")

    initialSticks = int(input("How many sticks are there on the table initially? [10-100]"))
    print ("How many sticks are there on the table initially? [10-100]", initialSticks)

    
    while initialSticks > 100 or initialSticks <10:

        print ("Please enter a number between 10-100")

        initialSticks = int(input("How many sticks are there on the table initially? [10-100]"))

        print ("How many sticks are there on the table initially? [10-100]", initialSticks)

        initialSticks = initialSticks

    return initialSticks
def checkPickedSticks1 ():
    pickedSticks = int(input("Player 1: How many sticks do you pick?[1-3]"))
    print ("Player 1: How many sticks do you pick?[1-3]" , pickedSticks)
    while pickedSticks > 3 or pickedSticks <1:

        print ("Please enter a number between 1-3")

        pickedSticks = int(input("Player 1: How many sticks do you pick?[1-3]"))

        print ("Player 1: How many sticks do you pick?[1-3]", pickedSticks)

        pickedSticks = pickedSticks

    return pickedSticks   
def checkPickedSticks2 ():
    pickedSticks = int(input("Player 2: How many sticks do you pick?[1-3]"))
    print ("Player 2: How many sticks do you pick?[1-3]" , pickedSticks)
    while pickedSticks > 3 or pickedSticks <1:

        print ("Please enter a number between 1-3")

        pickedSticks = int(input("Player 2: How many sticks do you pick?[1-3]"))

        print ("Player 2: How many sticks do you pick?[1-3]", pickedSticks)

        pickedSticks = pickedSticks

    return pickedSticks   

def countRemainingSticks():
    initialSticks = setInitialSticks ()
    pickedSticks = initialSticks
    n = 0 
    while pickedSticks > 1:
        print ("There are " + str(pickedSticks) + " on the board")
        if n%2 == 0: newPickedSticks = checkPickedSticks1()
        elif n%2 == 1: newPickedSticks = checkPickedSticks2()
        pickedSticks = pickedSticks - newPickedSticks
        if pickedSticks <= 1: print ("You loser")
        n = n+1
    return 
print(countRemainingSticks ())
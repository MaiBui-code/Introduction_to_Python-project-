import random
def readWords(inputFile):
    with open (inputFile, "r") as reader:
        outputList = []
        for line in reader:
            newLine = line.strip()
            newLine = newLine.lower()
            outputList.append(newLine)
        return outputList
def displaySandwich(sandwich):
    displayedSandwich = "\n".join(sandwich)
    return displayedSandwich
#print(readWords("scrabble5.txt"))
#print(displaySandwich(["-----", "-----","-----"]))
def updateBread(hiddenWord, userWord, sandwich):
    #sandwich = ["-----", "-----","-----"]
    scrabble5List = readWords("scrabble5.txt")
#    print(scrabble5List)
    positionHidden = scrabble5List.index(hiddenWord)
    topList = scrabble5List[:positionHidden]
    bottomList = scrabble5List[positionHidden+1:]
    if userWord in topList: 
        sandwich[0] = userWord
    elif userWord in bottomList:
        sandwich[2] = userWord
    elif userWord == hiddenWord:
        sandwich[1] = userWord
    return sandwich
#print(updateBread("acorn", "abrim", ["-----", "-----","-----"]))
def checkWord(userWord, aList):
    if userWord in aList:
        return userWord
    elif userWord == "q":
        return "q"
    else: 
        return "Oops! That doesn't seem to be a 5-letter word..."

def playGame(hiddenWord, validWordList):
    '''
    the playGame function is the main game function for wordSandwich. It takes a
    string representing the word that the user must find and a list of words that
    the user is allowed to guess.  This function manages the main gameplay of
    word sandwich.  It should return True if the user has found the word or False
    if the user has given up and typed 'q' to quit.

    parameters:
      hiddenWord    -   (string) the word that the user must guess
      validWordList -   (list of strings) list of valid words that the user can
                        guess from

    output:
      returns  -  (boolean) True if the user wins, False if they quit'''
    sandwich = ["-----", "-----","-----"]
    while True:
        # ask to enter
        userWord = input("Enter a 5-letter word or q to quit: ")
        checkedUser = checkWord(userWord, validWordList)
        if checkedUser == "q": 
            return False
        #while (sandwich != ["-----", hiddenWord, "-----"]) or (checkedUser!= "q"): 
        elif checkedUser == hiddenWord: 
            updatedSandwich = updateBread(hiddenWord,checkedUser,sandwich)
            sandwich = updatedSandwich
            print(displaySandwich(sandwich))
            return True
        # updatebread()
        #sandwich[1] = hideenrword
        #return True
        elif checkedUser == userWord: 
            updatedSandwich = updateBread(hiddenWord,checkedUser,sandwich)
            sandwich = updatedSandwich  
            print(displaySandwich(sandwich))  
            
            #userWord = input("Enter a 5-letter word or quit ")
            #checkedUser = checkWord(userWord, validWordList)             
        elif checkedUser == "Oops! That doesn't seem to be a 5-letter word...":
            userWord = input("Please enter a 5-letter word or quit: ")
            checkedUser = checkWord(userWord, validWordList)
            if checkedUser == userWord: 
                updatedSandwich = updateBread(hiddenWord,checkedUser,sandwich)
                sandwich = updatedSandwich  
                print(displaySandwich(sandwich))
                    
        
def main ():
    print("Welcome to word sandwich! \nTry to guess the secret word by entering 5-letter words. \nAs you guess, your words will form a sandwich to help guide you. \nhe secret word will be sandwiched between the top and bottom bread!")
    print ("Play the game")
    #sandwich = ["-----", "-----","-----"]
    #print(displaySandwich(sandwich))
    common5List = readWords("common5.txt")
    hiddenWord = random.choice(common5List)
    #print(hiddenWord)
    scrabble5List = readWords("scrabble5.txt")
    if playGame(hiddenWord, scrabble5List):
       print ("Well done, the word was ", hiddenWord)
    else:
        print ("So sorry, the word was ", hiddenWord)
print(main())




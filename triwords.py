import random
fromText = "ban"
toText = "???"
def main():
    print("Welcome to Triwords!")
    print("You'll have 5 guesses to figure out a secret word.")
    print("The word uses only 3 letters!")
    print("??????")
    guess = 5
    summ = 0
    correctAnswer = "??????" 
    money = 1
#run the for loop to make the repetition for each guess 
#stop when guess = 5 or when go bamkrupt
    while (guess > 0) and (correctAnswer!= "banana") and (money>0):
        money = generateMoney()
        print("Time to spin the wheel...\nYou are playing this round for", money)
  
#check whether money is 0 or not:
        if money == 0: return "You go bankrypt"
        else: 
            letter = input("Guess a letter: ")
#check whether the letter is in the "banana" or not
            letterChecked = checkLetter(letter)
#If the letter is in the "banana", make the trans
            if letterChecked == letter: 
# count the right letter appears how many times in the right word
                count = "banana".count(letterChecked)
#Print out money the player get after getting the right answer
                summ = summ + money*count
#Replace the ? with the letter to form a new toText: ex: ??? -> ?a? 
                newToText = findAndReplace(letterChecked)
#Take the fromText and toText and translate to get the true Code 
                firstRightAnswer = maketrans(fromText,newToText)
#After have the firstRightAnswer, add it to the correct answer. 
# After getting the second right answer, add it to the correct answer
                fromText2 = firstRightAnswer
                toText2 = correctAnswer
                for letter in firstRightAnswer:
                    fromText2 = firstRightAnswer
                    toText2 = correctAnswer
                    if letter in "ban":
                        if letter == "b": count = 1
                        elif letter == "a" : count = 6
                        elif letter == "n": count = 4
                        for number in range (0,count):
                            letterPosition2 = fromText2.find(letter, number)
                            toTextList2 = list(toText2)
                            toTextList2[letterPosition2] = letter
                            correctAnswer = "".join(toTextList2)
                            toText2 = correctAnswer
                print (correctAnswer)
                #numberOfLetters = correctAnswer.count(letter)
                #print (numberOfLetters)
                #summ = summ + money*numberOfLetters
                if correctAnswer == "banana": print ("Congratulation, you won this with ", summ)
#If the letter is not in the "banana": print go bankrupt
            else:
                print (letterChecked)
                summ = summ + 0 
            print ("Your bank currently has,", summ)
            guess = guess - 1     
#randomly choose the money
def generateMoney():
    money = random.randint(0,4000)
    return money
#check if letter in the keyword
def checkLetter(letter):
    if letter in "ban": 
        print ("You guessed one of the letter")
        return letter
    else: return "Too bad, " + letter + " is not in the word."
#find where is the letter position and replace ? with it
def findAndReplace(letter):
    letterPosition = fromText.find(letter)
    toTextList = list(toText)
    toTextList[letterPosition] = letter
    newToText = "".join(toTextList)
    return newToText

#implement maketrans to trans the ??? into right code
def maketrans(fromText,toText):
    trans_table = str.maketrans(fromText, toText)
    secret_code = "banana".translate(trans_table)
    return (secret_code)

main()


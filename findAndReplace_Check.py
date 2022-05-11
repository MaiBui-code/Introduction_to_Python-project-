fromText = "ban"
toText = "???"
letter = "a"
letterPosition = fromText.find(letter)
toTextList = list(toText)
toTextList[letterPosition] = letter
newToText = "".join(toTextList)
print (newToText)
print (toTextList)


for letter in "?a?a?a":
    fromText = "?a?a?a"
    toText = "b?????"
    if letter in "ban":
        for number in range (0,6):
            letterPosition = fromText.find(letter, number)
            toTextList = list(toText)
            toTextList[letterPosition] = letter
            correctAnswer = "".join(toTextList)
            toText = correctAnswer
print (correctAnswer)
def countLetter(infile):
    letterCount = {}
    with open (infile, "r") as reader:
        for line in reader:
            lineContents = line.strip()
            for letter in lineContents:
                if letter in letterCount:
                    letterCount[letter] = letterCount[letter] + 1
                else: 
                    letterCount[letter] = 1
    return letterCount

print(countLetter("scrabble.txt"))
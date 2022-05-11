def findPermutations(s):
    if len(s) == 0:
        return [""]
    elif len(s) ==1:
        return [s]
    else: 
        resultList = []
        for letter in s:
            remainLetters = s.replace(letter, '', 1)
            smallFindPermutations = findPermutations(remainLetters)
            for word in smallFindPermutations:
                result = letter + word
                resultList.append(result)
        return resultList
def anagrams( s, validWords ):
    """Given a string s and list of valid words, return a list of all anagrams
  (permutations of s that are valid) of the letters of s.
  This includes the input itself if it is a word. If no anagrams can be found,
  returns the empty list. """
    result = []
    permutationsOfS = findPermutations(s)
    for permutation in permutationsOfS:
        if permutation in validWords: 
            result.append(permutation)
    resultSet = list(set(result))
    return resultSet

def readValidWords(file):
    result = []
    with open(file, "r") as reader:
        for line in reader:
            lowLine = line.lower()
            result.append(line)
            print(result)
        return result
    return []

validWordsList = readValidWords("scrabble.txt")
print(anagrams("team", validWordsList))

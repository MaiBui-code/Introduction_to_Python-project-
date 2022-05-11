import random
def main():
    playerChoice = input("What do you want to bet [odd/even]? ")
    playerNumberString = input("What number of fingers do you want to show [0-5]? ")
    compNumber = generateCompNumber()
    print ("The computer goes with: ", compNumber)
    playerNumber = int(playerNumberString)
    sumOddOrEven1 = sumOddOrEven(playerNumber,compNumber)
    result = decideWhoWin(playerChoice,sumOddOrEven1)
    return result 
def generateCompNumber():
    compNumber = random.randint(0,5)
    return compNumber
def sumOddOrEven(playerNum,compNum):
    sum = playerNum + compNum
    if sum%2 ==  0: return "even" 
    else: return "odd"
def decideWhoWin(playerChoice,sumOddOrEven):
    if playerChoice == sumOddOrEven: return "You win"
    else: return "You lose"

a = main()
print (a)

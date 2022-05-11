import random
#     playtherockpaperscissors:
def main ():
#   * Ask user if they want rock, paper, or scissors
    userChoice = input("Welcome to rock, paper, scissors. Choose your item: [r,p,s] ")
#   Return error and print Please ... if userChoice is different from r,p,s
    if userChoice in " r p s": 
#     * Call the function to generate the computer choice
        compChoice = generateCompChoice()
#     * Call the function to determine the winner
        result = determineTheWinner(userChoice, compChoice)
        print ("The computer goes with: ", compChoice)
        print ("so winner issssss: ",result)
    else: 
        print ("Please give r, p or s")
        return "Error"
        

#     Generate computer choice: 
def generateCompChoice():
    compChoice = random.randint (0,2)
    if compChoice == 0: return "r"
    elif compChoice == 1: return "p"
    elif compChoice == 2: return "s"
#     Determine the winner:
def determineTheWinner(userChoice,compChoice):
    if userChoice == "r": 
        if compChoice == "p": return "computer"
        elif compChoice == "s": return "user"
        else: return "tie"
    if userChoice == "p":
        if compChoice == "p":return "tie"
        elif compChoice == "s": return "computer"
        else: return "user"
    if userChoice == "s":
        if compChoice == "p": return "user"
        elif compChoice == "s": return "tie"
        else: return "computer"
    return
main()


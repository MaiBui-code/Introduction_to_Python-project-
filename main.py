from Player import Player
from Card import Card
from CityLineGame import CityLineGame
def main():
    print("""Welcome to CityLine!
In this game, each player has a hand of cards with city names on them.
You must order them by the temperature recorded on August 23, 1989. Taking turns,
each player will attempt to put their next card in the right spot.
Press q to quit at any time.""")
    numPlayers = int(input("How many players are there? [1-6]"))
    #prompts the user for the number of players (ensuring that they enter a number between 1 and 6, inclusive)
    if (numPlayers >=  1) and (numPlayers <=  6):
        #creates a new instance of the CityLineGame
        game = CityLineGame("August23-1989-temps5.json", numPlayers)
        #plays the game by invoking its instance method playGame
        game.playGame()
main()

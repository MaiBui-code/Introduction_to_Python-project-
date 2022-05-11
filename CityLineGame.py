import random
from Player import Player
from Card import Card
class CityLineGame(object):
    def __init__(self, jsonFile, numPlayers):
        #initialize a cardLine instance property to be an empty list (this will track the cards as they are inserted in order)
        self.__deck = self.readCardsFromJson(jsonFile)
        #initialize a cardLine instance property to be an empty list (this will track the cards as they are inserted in order)
        self.__cardLine = []
        #invoke an instance method initPlayers
        self.__players = self.initPlayers(numPlayers)
        #invoke an instance method dealCards
        self.dealCards()
    def readCardsFromJson(self,jsonFile):
        card = []
        with open (jsonFile, "r") as reader:
            for line in reader:
                card.append(Card(line, reader[line]))
            return card
    def initPlayers(numPlayers):
        name = []
        for i in range(numPlayers):
            name.append((input(f"What is the player {i} names?")))
            return name
    def dealCards (self,numPlayers):
        #shuffle the deck
        random.shuffle(self.__deck)
        #reveal and “deal” a card into the cardLine instance 
        print(f"The first card is {self.__deck[0].getInfo()}")
        self.__cardLine.append(self.__deck[0])
        self.__deck.pop(0)
        #“deal” the remaining cards into the players’ hands 
        #rotating through using the pop method again
        i = 0
        while self.__deck != []:
            #to give the right card to the right player, we can use %
            self.__players[i].addCard(self.__deck(0))
            self.__deck.pop(0)
            i = i + 1
            if i == (numPlayers-1):
                i = i - (numPlayers-1)
        #playGame() At each rotation (iteration), you should invoke the instance method playRound. Once the game is over, it should print out something like the following, using the instance method displayPlayerScores to help:
    def playGame(self):
        #The method should rotate through the players until finding a player has no cards remaining.      
        for player in self.__players:
            #At each rotation (iteration), you should invoke the instance method playRound
            if player.hasCards() == True:
                self.playRound()
            #if the game is over
            else:
                #print using the method displayPlayerScores
                self.displayPlayerScores()
    def playRound( self,player,numPlayers ):
        #print out the current state of the game using the instance method displayGame
        self.displayGame()
        for player in self.__players:
            #use the player’s instance method dealCard to deal their next card
            playerCard = player.dealCards(numPlayers)
            #print the card’s info using the card’s intance method getInfo
            print(f"{player} your card is: {playerCard.getInfo()}")
            
            #prompt the user to decide where the card should go
            print("Which card do you think it should come before in the line?")
            userPos = input(f"Enter {len(self.__cardLine)} if you think should go at the end.")
                  
            #reveal the card and print out the info again
            playerCard.reveal()
            print(f"The complete info on your card was: {playerCard.getInfo()}")
                  
            #check if the user is correct using the instance method correctPosition
            result = self.correctPosition(userPos, playerCard)
            
            #if it is the right position
            if result == True:
                #notify the user 
                print("You are right!")
                #insert the card into the cardLine at that index 
                self.__cardLine.insert(userPos, playerCard)
                #add a point to the player
                player.addPoint()
                  
            #if not, simply notify the user (the card is “discarded”)
            else:
                  print("The card is discarded")
      
    def displayGame(self):
        #print out the player scores using the instance method printPlayerScores 
        self.printPlayerScore()
        #before printing each card in the cardLine. 
        for card in self.__cardLine:
            #When printing a card, put its index (starting at 0) followed by a tab (using the \t special character)
            #invoking the card’s instance method getInfo.
            print(f"{self.__cardLine.index(card)} \t {card.getName()} : {card.getData()}") 
    def printPlayerScore(self):
        for player in self.__players:
            print(f"{player}: {player.getPoints()}")
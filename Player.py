class Player(object):
    def __init__(self, name):
        self.__name = name
        self.__handCards = []
        self.__points = 0
    def getName(self):
        return self.__name
    def getPoints(self):
        return self.__points
    def hasCards(self):
        if len(self.__handCards) > 0:
            return True
        else:
            return False
    def addCard(self,card):
        self.__handCards.append(card)
    def addPoint(self):
        self.__points += 1
    def dealCard(self):
        if len(self.__handCards) == 0:
            return None
        else: 
            self.__discardedCard = self.__handCards[0]
            self.__handCards.pop(0)
            return self.__discardedCard
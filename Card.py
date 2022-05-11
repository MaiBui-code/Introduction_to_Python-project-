class Card(object):  
    def __init__(self, city, data):
        self.__name = city
        self.__data = data
        self.__revealed = False
    def getData(self):
        return self.__data
    def getInfo(self):
        if self.__revealed == False:
            return self.__name
        else:
            return self.__name + ": " + str(self.__data)
    def reveal(self):
        self.__revealed = True
        return self.__revealed
first = Card("Nairobi", 68)
first.reveal()
first.getInfo()
        
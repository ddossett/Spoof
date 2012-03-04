import random
from PlayerTable import PlayerTable

class BaseBrain:
    """Base class for players"""
    __name__ = "BaseBrain"

    def __init__(self,playerTable,playerTables,minCoins=0,maxCoins=3):
        self.minCoins = minCoins
        self.maxCoins = maxCoins
        self.numCoins = 0
        self.guessCoins = 0
        self.playerTables = playerTables
        self.pt = playerTable

    def Throw(self):
        self.numCoins = random.randint(self.minCoins,self.maxCoins)
        return self.numCoins
    
    def Guess(self):
        self.maxGuess=len(self.playerTables * self.maxCoins) + self.numCoins - self.maxCoins
        self.guessCoins = random.randint(self.numCoins,self.maxGuess)
        return self.guessCoins

    def __str__(self):
        return self.__class__.__name__+':'+self.pt.name
    
    def __repr__(self):
        return self.__class__.__name__+':'+self.pt.name

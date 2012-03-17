import utils
from getpass import getpass
import math
from scipy.misc import comb
import random
from data import PlayerTable as PT

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

class Human(BaseBrain):
    """Interface for Human player, derived from BaseBrain class. 'Human' provides the prompting/error checking interface for a human player's throws and guesses."""
    __name__ = "Human"

    def Throw(self):
        """Prompt for human input"""
        promptString = 'enter your number of coins: '
        thrown = False
        while thrown==False:
            tmpNumCoins = getpass(prompt='\n'+self.pt.name+' '+promptString)
            if utils.checkInt(tmpNumCoins):
                tmpNumCoins = int(tmpNumCoins)
                if tmpNumCoins<=self.maxCoins and tmpNumCoins>=self.minCoins:
                    self.numCoins = tmpNumCoins
                    thrown = True
                else:
                    print '\nThat wasn\'t a valid number of coins to throw. Please try again.'
                    continue
            else:
                print '\nThe number you entered wasn\'t an integer. Please try again.'
                continue
        return self.numCoins

    def Guess(self):
        promptString = 'enter your guess for the total: '
        guessed = False
        while guessed==False:
            guess = raw_input('\n'+self.pt.name+' '+promptString)
            if utils.checkInt(guess):
                guess = int(guess)
                if guess>=self.numCoins and guess<=((len(self.playerTables) * self.maxCoins) + self.numCoins - self.maxCoins):
                    self.guessCoins = guess
                    guessed = True
                else:
                    print '\nThat wasn\'t in the range of valid guesses. Please try again.'
                    continue
            else:
                print '\nThe number you entered wasn\'t an integer. Please try again.'
                continue
        return self.guessCoins

class Hactar(BaseBrain):
    """Brain for Hactar computer player, derived from BaseBrain class. Hactar finds the most probable total sum assuming every player throws randomly."""
    __name__ = "Hactar"
    pass

    def CoinSumProb(self,k):
        i = 0
        prob = 0.0
        n = len(self.playerTables)
        k = k + (n*(self.minCoins-1))
        probs = []
        numStates = self.maxCoins - self.minCoins + 1.0
        if (k>=n and k<=(n*numStates)):
            prob = math.pow((1.0/numStates),n)
        oldasym = -1.0
        while i<=(math.floor((k-n)/numStates)):
            asym = math.pow(oldasym, i)
            probs.append(prob*asym*comb(n,i,exact=True)*comb((k-(int(numStates)*i)-1),(n-1),exact=True))
            i += 1
        totProb = sum(probs)
        return totProb

class Mycroft(BaseBrain):
    """Brain for Mycroft computer player, derived from BaseBrain class. Mycroft implements Markov analysis to guess each human player's throw."""
    __name__ = "Mycroft"
    pass

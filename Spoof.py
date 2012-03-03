import getpass
import sys
from random import randint,uniform,shuffle
import textwrap
from scipy.misc import comb
import math

from Checks import *
from PlayerTable import PlayerTable
from Hactar import Hactar
from Mycroft import Mycroft
from BaseBrain import BaseBrain
from Human import Human

class Spoof:
    """Class to run the game Spoof. Uses PlayerTable() to save/get information and the BaseBrain() derived Classes to make computer players"""
    __name__ = "Spoof"

    validComputerNames = ["Juan","Mohammed","Fatima","Isabel","Uri","Daniel","Sara","Charlie","Ben","Marie","Emma","Liam","James","Olivia","Mary"]

    def __init__(self):
        self.players = []
        self._winnerFlag = False
        self.titleCard()
        description = 'This is a game for as many human players as you want, the number of computer players is limited by the len(Spoof.validComputerNames). Once you\'ve setup the game you should each think of a number of coins between 0 and 3 and enter it (covertly) when prompted. Then when asked, enter in your guess for the total number of coins. The winner gets to leave the game and the remaining players continue until there is a loser. Easy!'
        print textwrap.fill(description,width=60)
        shuffle(Spoof.validComputerNames)
        self._setPlayers()
#        while (self._winnerFlag==False):
#            self._runRound()

    def titleCard(self):
        """Prints out the titlecard for the game"""
        str_Welcome = 'Welcome to Spoof'
        print
        print ('{:/^20}'.format('')).center(60)
        print ('{:/^20}'.format(str_Welcome)).center(60)
        print ('{:/^20}'.format('')).center(60)
        print

    def _setPlayers(self):
        numPlayers = 0
        compNameIndex = 0
        while numPlayers==0:
            tmpNumPlayers = getpass.getpass(prompt='\nHow many players do you want?')
            if checkInt(tmpNumPlayers):
                numPlayers = int(tmpNumPlayers)
            else:
                print '\nThat\'s not a valid number. Please try again.'
                continue
        for player in range(numPlayers):
            playerName = 'Player'+str((player+1))
            playerType = getpass.getpass(prompt='\n'+playerName+' is Human(0), BaseBrain(1), Hactar(2), or Mycroft(3)? Enter 0,1,2,3')
            if checkInt(playerType):
                playerType = int(playerType)
            if playerType!=0:
                playerName = Spoof.validComputerNames[compNameIndex % len(Spoof.validComputerNames)]
                compNameIndex += 1
            self.players.append( PlayerTable(playerName,playerType) )
    
    def _checkValidGuess(self,guess,numPlayers):
        """Checks that the passed guess is valid given the restrictions (must be between 0 and (Number of players)*3)"""
        maxCoins = numPlayers*3
        if guess<=maxCoins:
            return True
        else:
            return False

    def _getComputerThrow(self,i,list_Players):
        print '\n'+list_Players[i]+' is throwing...'
        tmpNumCoins = randint(0,3)
        return tmpNumCoins

    def _getThrow(self,i,list_Players,human=False):
        tmpNumCoins = 0
        if human:
            tmpNumCoins = self._getHumanThrow(i,list_Players)
        else: tmpNumCoins = self._getComputerThrow(i,list_Players)
        return tmpNumCoins

    def _getComputerGuess(self,i,list_Players):
        print '\n'+list_Players[i]+' is guessing...'
        maxCoins = len(list_Players)*3
        tmpGuess = randint(0,maxCoins)
        return tmpGuess

    def _getGuess(self,i,list_Players,human=False):
        guess = 0
        if human:
            guess = self._getHumanGuess(i,list_Players)
        else:
            guess = self._getComputerGuess(i,list_Players)
        return guess

    def _runRound(self):
    
        numCoins = [0]*len(self._list_Players)
        
        int_i = 0
        while int_i<len(self._list_Players):
            tmpNumCoins = self._getThrow(int_i,self._list_Players)
            if checkInt(tmpNumCoins):
                numCoins[int_i] = int(tmpNumCoins)
                int_i+=1
            else: continue
        
        int_Sum = 0
        for n in numCoins:
            int_Sum+=n
        
        guesses = [0]*len(self._list_Players)
        int_i = 0
        while int_i<len(guesses):
            tmpGuess = self._getGuess(int_i,self._list_Players)
            if checkInt(tmpGuess):
                print '\n'+self._list_Players[int_i]+' guessed',tmpGuess,"coins"
                if self._checkValidGuess(int(tmpGuess),len(guesses)):
                    guesses[int_i] = int(tmpGuess)
                    int_i+=1
                else:
                    print '\nThat\'s not a valid guess. Please try again'
                    continue
            else: continue
        
        print '\nSum of coins was',int_Sum
        str_CongratulateRound = 'wins this round!'
        int_j = 0
        winner = False
        for guess in guesses:
            if guess==int_Sum:
                print '\n'+self._list_Players[int_j],str_CongratulateRound
                winner=True
            int_j+=1
        
        if not winner: print '\nNoone won this round, try again.'

#def sumFairDiceProb(n,k):
#    i=0
#    probs=[]
#    prob = 0.0
#    if (k>=n and k<=(n*6)):
#        prob = math.pow((1.0/6.0),n)
##    print 'prob =',prob
#    oldasym = -1.0
#    print 'Floored max =',math.floor((k-n)/6)
#    while i<=math.floor((k-n)/6):
#        asym = math.pow(oldasym, i)
#        print 'i=',i
#        print 'asmy =',asym
#        print 'comb1 =',comb(n,i,exact=True)
##        print (k-(6*i)-1)
##        print n-1
#        print 'comb2 =',comb((k-(6*i)-1),(n-1),exact=True)
#        probs.append(prob*asym*comb(n,i,exact=True)*comb((k-(6*i)-1),(n-1),exact=True))
#        i+=1
#    print probs
#    totProb = sum(probs)
#    print totProb
#    return totProb

#def sumFairCoinProb(n,k):
#    i=0
#    k=k+n
#    probs=[]
#    prob = 0.0
#    if (k>=n and k<=(n*4)):
#        prob = math.pow((1.0/4.0),n)
##    print 'prob =',prob
#    oldasym = -1.0
#    print 'Floored max =',math.floor((k-n)/4)
#    while i<=math.floor((k-n)/4):
#        asym = math.pow(oldasym, i)
#        print 'i=',i
#        print 'asmy =',asym
#        print 'comb1 =',comb(n,i,exact=True)
##        print (k-(6*i)-1)
##        print n-1
#        print 'comb2 =',comb((k-(4*i)-1),(n-1),exact=True)
#        probs.append(prob*asym*comb(n,i,exact=True)*comb((k-(4*i)-1),(n-1),exact=True))
#        i+=1
#    print probs
#    totProb = sum(probs)
#    print totProb
#    return totProb

#ll = []
#ll.append(sumFairCoinProb(2,0))
#ll.append(sumFairCoinProb(2,1))
#ll.append(sumFairCoinProb(2,2))
#ll.append(sumFairCoinProb(2,3))
#ll.append(sumFairCoinProb(2,4))
#ll.append(sumFairCoinProb(2,5))
#ll.append(sumFairCoinProb(2,6))
#ll.append(sumFairCoinProb(2,7))
#print ll
#print sum(ll)

#print comb(6,1,exact = True)

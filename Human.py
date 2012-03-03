from BaseBrain import BaseBrain
from PlayerTable import PlayerTable
from Checks import *

class Human(BaseBrain):
    """Interface for Human player, derived from BaseBrain class. 'Human' provides the prompting/error checking interface for a human player's throws and guesses."""
    __name__ = "Human"

    def Throw(self):
        """Prompt for human input"""
        promptString = '\nenter your number of coins: '
        thrown = False
        while thrown==False:
            tmpNumCoins = getpass.getpass(prompt='\n'+self.pt.name+' '+promptString)
            if Checks.checkInt(tmpNumCoins):
                tmpNumCoins = int(tmpNumCoins)
                if tmpNumCoins<self.maxCoins and tmpNumCoins>self.minCoins:
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
        promptString = '\nenter your guess for the total: '
        guessed = False
        while guessed==False:
            tmpGuess = getpass.getpass(prompt='\n'+self.pt.name+' '+promptString)
            if Checks.checkInt(tmpGuess):
                tmpGuess = int(tmpGuess)
                if tmpGuess>self.numCoins and tmpGuess<(len(self.playerTables)-self.numCoins):
                    self.guessCoins = tmpGuess
                    guessed = True
                else:
                    print '\nThat wasn\'t in the range of valid guesses. Please try again.'
                    continue
            else:
                print '\nThe number you entered wasn\'t an integer. Please try again.'
                continue
        return self.guessCoins

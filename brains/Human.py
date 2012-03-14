from BaseBrain import BaseBrain as BB
#from PlayerTable import PlayerTable as PT
from Checks import *
from getpass import getpass

class Human(BB):
    """Interface for Human player, derived from BaseBrain class. 'Human' provides the prompting/error checking interface for a human player's throws and guesses."""
    __name__ = "Human"

    def Throw(self):
        """Prompt for human input"""
        promptString = 'enter your number of coins: '
        thrown = False
        while thrown==False:
            tmpNumCoins = getpass(prompt='\n'+self.pt.name+' '+promptString)
            if checkInt(tmpNumCoins):
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
            if checkInt(guess):
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

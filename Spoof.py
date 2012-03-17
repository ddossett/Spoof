from random import randint,uniform,shuffle
import textwrap
import brains
import utils
from data import PlayerTable as PT

class Spoof:
    """Class to run the game Spoof. Uses PlayerTable() to save/get information and the BaseBrain() derived Classes to make computer players"""
    __name__ = "Spoof"

    validComputerNames = ["Juan","Mohammed","Fatima","Isabel","Uri","Daniel","Sara","Charlie","Ben","Marie","Emma","Liam","James","Olivia","Mary"]

    def __init__(self):
        self.players = []
        self.playerBrains = []
        self._loserFlag = False
        self.TitleCard()
        description = 'This is a game for as many human players as you want, the number of computer players is limited by the len(Spoof.validComputerNames). Once you\'ve setup the game you should each think of a number of coins between 0 and 3 and enter it (covertly) when prompted. Then when asked, enter in your guess for the total number of coins. The winner gets to leave the game and the remaining players continue until there is a loser. Easy!'
        print textwrap.fill(description,width=60)
        shuffle(Spoof.validComputerNames)
        self._SetPlayers()
        while (self._loserFlag==False):
            self._RunRound()
        print '\n'+self.players[0].name, 'is the loser! Well played numbnuts!'

    def TitleCard(self):
        """Prints out the titlecard for the game"""
        str_Welcome = 'Welcome to Spoof'
        print
        print ('{:/^20}'.format('')).center(60)
        print ('{:/^20}'.format(str_Welcome)).center(60)
        print ('{:/^20}'.format('')).center(60)
        print

    def _SetPlayers(self):
        numPlayers = 0
        compNameIndex = randint(0,len(Spoof.validComputerNames))
        while numPlayers==0:
            tmpNumPlayers = raw_input('\nHow many players do you want? ')
            if utils.checkInt(tmpNumPlayers):
                numPlayers = int(tmpNumPlayers)
            else:
                print '\nThat\'s not a valid number. Please try again.'
                continue
        for player in range(numPlayers):
            playerName = 'Player'+str((player+1))
            name=False
            while name==False:
                playerType = raw_input('\n'+playerName+' is Human(0), BaseBrain(1), Hactar(2), or Mycroft(3)? Enter 0,1,2,3: ')
                if utils.checkInt(playerType):
                    playerType = int(playerType)
                    name=True
            if playerType!=0:
                playerName = Spoof.validComputerNames[compNameIndex % len(Spoof.validComputerNames)]
                compNameIndex += 1
            else:
                playerName = raw_input('\nEnter the name for this Human player: ')
            self.players.append( PT(playerName,playerType) )
   
    def _SetBrains(self):
        for player in self.players:
            if player.playerType=='Human':
                self.playerBrains.append(brains.Human(player, self.players))
            elif player.playerType=='BaseBrain':
                self.playerBrains.append(brains.BaseBrain(player, self.players))
            elif player.playerType=='Hactar':
                self.playerBrains.append(brains.Hactar(player, self.players))
            else: pass
        return True

    def _RunRound(self):
        self._SetBrains()
#        print self.playerBrains
#        print self.players
        sumCoins = 0
        # Get the throws of each player
        for i,pb in enumerate(self.playerBrains):
            throw = pb.Throw()
            self.players[i].table[len(self.players)] = [throw]
            sumCoins+=throw

        # Get the guesses of each player
        for i,pb in enumerate(self.playerBrains):
            guess = pb.Guess()
            self.players[i].table[len(self.players)].append(guess)

#        for pt in self.players:
#            print '\n'+pt.name+':\n'+str(pt.table)

        print '\nSum of coins was',sumCoins
        congratulate = 'wins this round!'
        winner = False
        for i,player in enumerate(self.players):
            guess = player.table[len(self.players)][1]
            if guess==sumCoins:
                print '\n'+player.name, congratulate
                winner=True
                self.players.pop(i)
                if len(self.players)<2:
                    self._loserFlag=True
                break
        
        if not winner: print '\nNoone won this round, try again.'
        self.playerBrains = []
        return True

if __name__=='__main__':
    Spoof()

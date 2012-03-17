import numpy

class PlayerTable:
    """Class to hold and interface with information about players in the game, their names/throws/guesses/brain type etc"""
    __name__ = "PlayerTable"

    validPlayerTypes = ["Human","BaseBrain","Hactar","Mycroft"]

    def __init__(self,playerName,playerType=0):
        self.name = playerName
        self.playerType = PlayerTable.validPlayerTypes[playerType]
        self.table = {}

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

def fakeThrows(rows=100):
    """Generate toy data in the format [ throw, previousthrow, previouspreviousthrow, numplayers ]
and output it to data.txt"""
    from brains import BaseBrain as BB
    import random
    columns = 4
    rawData = numpy.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
            if j<3:
                rawData[i,j] = random.randint(0,3)
            else:
                rawData[i,j] = random.randint(2,5)
    numpy.savetxt("data.txt",rawData,fmt='%.5f')

def createDist(fileName='data.txt'):
    """Function to read in a ndarray from a file and create the probability distribution for a human player's throw in different situations (round, previous throws).
    
    Then write the data out ready to be used by a brain."""
    import scipy
    rawData = numpy.genfromtxt(fileName)

    throws = rawData[:,0]
    h = scipy.histogram(throws,4)
    print h
    weights = numpy.zeros(4)
    rows = throws.size
    for throw in range(4):
        weights[throw] = h[0][throw]/rows
    numpy.savetxt("weights.txt", weights,fmt='%.5f')
    return data
    
def createUniformWeights():
    """The weights file will have numpy arrayed data in the format
    (numplayers, previous throw, pre-pre throw, weight0, weight1, weight2, weight3)
    weight# are the probabilities of this person throwing #-coins
    
    This Function creates the weights.txt file filled with uniform probabilities for
    a large number of possible numplayers, so that we can read in from it as a template
    and re-assign the weights once we have the statistics."""

    maxplayers = 25
    choices = 4
    weightData = numpy.zeros(((maxplayers-1)*4*4,7),dtype=float)
    for numplayers in range(2,maxplayers+1):
        for preThrow in range(choices):
            for prepreThrow in range(choices):
                for weight in range(choices):
                    prob = 0.25
                    weightData[numplayers,:] = numpy.array([numplayers,preThrow,prepreThrow,prob,prob,prob,prob])
    numpy.savetxt('weights.txt',weightData,fmt='%.5f')

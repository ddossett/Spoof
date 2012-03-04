from BaseBrain import BaseBrain
import math
from scipy.misc import comb

class Hactar(BaseBrain):
    """Brain for Hactar computer player, derived from BaseBrain class. Hactar finds the most probable total sum assuming every player throws randomly."""
    __name__ = "Hactar"
    pass

    def CoinSumProb(self,k):
        i = self.minCoins
        prob = 0.0
        n = len(self.playerTables)
        k = k + n
        probs = []
        numStates = self.maxCoins - self.minCoins + 1.0
        if (k>=n and k<=(n*numStates)):
            prob = math.pow((1.0/numStates),n)
        oldasym = -1.0
        while i<=math.floor((k-n)/numStates):
            asym = math.pow(oldasym, i)
            probs.append(prob*asym*comb(n,i,exact=True)*comb((k-(numStates*i)-1),(n-1),exact=True))
            i += 1
        totProb = sum(probs)
        return totProb


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

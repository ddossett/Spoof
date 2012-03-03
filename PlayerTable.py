class PlayerTable:
    """Class to hold and interface with information about players in the game, their names/throws/guesses/brain type etc"""
    __name__ = "PlayerTable"

    validPlayerTypes = ["Human","Base","Hactar","Mycroft"]

    def __init__(self,playerName,playerType=0):
        self.name = playerName
        self.playerType = PlayerTable.validPlayerTypes[playerType]
        self.table = []

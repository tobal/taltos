
from src.CommonModules.Constants import gameModes

class GameMode(object):

    def __init__(self):
        self.mode = gameModes.RPG
    
    def setGameMode(self, gameMode):
        self.mode = gameMode
        
    def getGameMode(self):
        return self.mode
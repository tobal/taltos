
from CommonModules.Constants import GameModes

class GameMode(object):

    def __init__(self, gameMode):
        self.mode = gameMode
    
    def setGameMode(self, gameMode):
        self.mode = gameMode
        
    def getGameMode(self):
        return self.mode

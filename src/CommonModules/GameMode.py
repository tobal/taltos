
from src.CommonModules.Constants import GameModes

class GameMode(object):

    def __init__(self):
        self.mode = GameModes.RPG
    
    def setGameMode(self, gameMode):
        self.mode = gameMode
        
    def getGameMode(self):
        return self.mode
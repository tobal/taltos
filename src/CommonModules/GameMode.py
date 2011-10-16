
from src.CommonModules.Constants import gameModes

class GameMode():

    def __init__(self):
        self.mode = gameModes.RPG
    
    def setGameMode(self, gameMode):
        self.mode = gameMode
        
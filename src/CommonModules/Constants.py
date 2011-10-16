
from src.CommonModules.Constants import gameModes

class gameModes():

    def __init__(self):
        self.RPG = 0
        self.CYBERSPACE = 1
        self.WORKSHOP = 2
        self.HACKING = 3

class colors():
    
    def __init__(self):
        return
    
    def getBackgroundColor(self, gameMode):
        if gameMode == gameModes.RPG:
            return (255,255,255)
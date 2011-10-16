
class gameModes():

    RPG = 0
    CYBERSPACE = 1
    WORKSHOP = 2
    HACKING = 3

class colors():
    
    def __init__(self):
        return
    
    def getBackgroundColor(self, gameMode):
        if gameMode == gameModes.RPG:
            return (255,255,255)
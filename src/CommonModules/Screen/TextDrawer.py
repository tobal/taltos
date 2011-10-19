
from pygame.font import *
from src.CommonModules.Constants import gameModes

class TextDrawer(object):

    def __init__(self):
        self.rpgFont = Font("../resrc/fonts/gorrisans.ttf", 40)
        self.rpgRovas = Font("../resrc/fonts/rovmajb.ttf", 70)
        return
    
    def getFont(self, gameMode):
        if( gameMode == gameModes.RPG):
            return self.rpgFont
        return
    
    def getRovasFont(self, gameMode):
        if( gameMode == gameModes.RPG):
            return self.rpgRovas
        return
    
    
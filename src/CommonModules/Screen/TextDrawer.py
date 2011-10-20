
from pygame.font import *
from src.CommonModules.Constants import GameModes
from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import Colors

class TextDrawer(object):

    def __init__(self):
        self.menuFont = Font("../resrc/fonts/gorrisans.ttf", 40)
        self.menuRovas = Font("../resrc/fonts/rovmajb.ttf", 70)
        return
    
    def getFont(self, gameMode):
        if( gameMode == GameModes.MENU ):
            return self.menuFont
        return
    
    def getRovasFont(self, gameMode):
        if( gameMode == GameModes.MENU ):
            return self.menuRovas
        return
    
    def getTextSurface(self, text, gameMode, language):
        if( language == Languages.ROV ):
            font = self.getRovasFont(gameMode)
        else:
            font = self.getFont(gameMode)
        fgColor = Colors.getForegroundColor(Colors(), gameMode)
        bgColor = Colors.getBackgroundColor(Colors(), gameMode)
        normal_surface = font.render(text, True, fgColor, bgColor)
        inverse_surface = font.render(text, True, bgColor, fgColor)
        surface = {'normal':normal_surface, 'inverse':inverse_surface}
        return surface
    
    def getTextArraySurfaces(self, textArray, gameMode, language):
        output = []
        for txt in textArray:
            output.append(self.getTextSurface(txt, gameMode, language))
        return output
    

from pygame.font import *
from src.CommonModules.Texts.TextGetter import TextGetter 
from src.CommonModules.Constants import GameModes
from src.CommonModules.Constants import Languages
from src.CommonModules.Constants import Colors
from src.CommonModules.Constants import FontSizes
from src.CommonModules.Constants import TextSurfaceTypes

class TextDrawer(object):

    def __init__(self):
        self.menuFontBig = Font("../resrc/fonts/gorrisans.ttf", 40)
        self.menuRovasBig = Font("../resrc/fonts/rovmajb.ttf", 70)
        self.menuFontSmall = Font("../resrc/fonts/gorrisans.ttf", 24)
        self.menuRovasSmall = Font("../resrc/fonts/rovmajb.ttf", 40)
        return
    
    def getFont(self, gameMode, fontSize):
        if( gameMode == GameModes.MENU ):
            if( fontSize == FontSizes.BIG):
                return self.menuFontBig
            else:
                return self.menuFontSmall
        return
    
    def getRovasFont(self, gameMode, fontSize):
        if( gameMode == GameModes.MENU ):
            if( fontSize == FontSizes.BIG):
                return self.menuRovasBig
            else:
                return self.menuRovasSmall
        return
    
    def getTextSurface(self, text, gameMode, language, fontSize):
        if( language == Languages.ROV ):
            font = self.getRovasFont(gameMode, fontSize)
        else:
            font = self.getFont(gameMode, fontSize)
        fgColor = Colors.getForegroundColor(Colors(), gameMode)
        bgColor = Colors.getBackgroundColor(Colors(), gameMode)
        normal_surface = font.render(text, True, fgColor, bgColor)
        inverse_surface = font.render(text, True, bgColor, fgColor)
        surface = {TextSurfaceTypes.NORMAL : normal_surface, TextSurfaceTypes.INVERSE : inverse_surface}
        return surface
    
    def getTextArraySurfaces(self, textArray, gameMode, language, fontSize):
        output = []
        for txt in textArray:
            output.append(self.getTextSurface(txt, gameMode, language, fontSize))
        return output
    
    def getSurfaceArrayForCommonText(self, textType, gameMode, language, fontSize):
        textArray = TextGetter().getCommonText(textType, language)
        return self.getTextArraySurfaces(textArray, gameMode, language, fontSize)
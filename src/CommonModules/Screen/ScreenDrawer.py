
from src.CommonModules.Constants import colors

class ScreenDrawer(object):

    def __init__(self):
        return
    
    def fillWithBackgroundColor(self, screen, gameMode):
        bgColor = colors.getBackgroundColor(self, gameMode)
        screen.fill(bgColor)
        return
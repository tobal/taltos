
from src.CommonModules.Constants import colors
from pygame import draw
from pygame import Rect

class ScreenDrawer(object):

    def __init__(self):
        return
    
    def fillWithBackgroundColor(self, screen, gameMode):
        bgColor = colors.getBackgroundColor(colors(), gameMode)
        screen.fill(bgColor)
        return
    
    def drawBox(self, outerRect, frame, screen, gameMode):
        fgColor = colors.getForegroundColor(colors(), gameMode)
        bgColor = colors.getBackgroundColor(colors(), gameMode)
        innerRect = Rect((outerRect.left - frame, outerRect.top - frame),
                         (outerRect.width + frame*2, outerRect.height + frame*2))
        draw.rect(screen, fgColor, innerRect)
        draw.rect(screen, bgColor, outerRect)        
        return
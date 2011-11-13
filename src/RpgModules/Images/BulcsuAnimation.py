
from src.CommonModules.Screen.ImageHandler import ImageHandler
from src.CommonModules.Constants import Directions

class BulcsuAnimation():
    
    def __init__(self):
        rightwalk = []
        rightwalk.append(ImageHandler().loadImage("jobbraall"))
        for x in range(1, 7):
            rightwalk.append(ImageHandler().loadImage("jobbralep" + str(x)))

        leftwalk = []
        leftwalk.append(ImageHandler().loadImage("balraall"))
        for x in range(1, 7):
            leftwalk.append(ImageHandler().loadImage("balralep" + str(x)))
            
        self.FRAMES = {
                Directions.UP : [ 
                        ImageHandler().loadImage("hattalall"),
                        ImageHandler().loadImage("hattallep1"),
                        ImageHandler().loadImage("hattalall"),
                        ImageHandler().loadImage("hattallep2"),
                        ImageHandler().loadImage("hattalall") ],
                Directions.DOWN : [
                        ImageHandler().loadImage("szembenall"),
                        ImageHandler().loadImage("szembenlep1"),
                        ImageHandler().loadImage("szembenlep2"),
                        ImageHandler().loadImage("szembenlep3"),
                        ImageHandler().loadImage("szembenlep2") ],
                Directions.LEFT : leftwalk,
                Directions.RIGHT : rightwalk        
        }
        return
    
    def getAnimation(self, direction):
        return self.FRAMES[direction]
    
    def getAnimationFrame(self, direction, frame):
        return self.FRAMES[direction][frame]
    
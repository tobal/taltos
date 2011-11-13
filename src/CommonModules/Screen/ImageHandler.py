
from pygame.image import load

class ImageHandler():

    def __init__(self):
        pass

    def loadImage(self,  imageName,  alpha = True):
        imagePath = "../resrc/img/RPG/" + imageName + ".png"
        if alpha:
            img = load(imagePath).convert_alpha()
        else:
            img = load(imagePath).convert()
        return img

import pygame.image
from src.RpgModules.BoundingBox import BoundingBox

class Object(object):

    def __init__(self, x, y, dimX, dimY):
        self.pos = [x, y]
        self.dimensions = [dimX, dimY]
        self.bBox = BoundingBox(x, y, x + dimX, y + dimY)
        return

    def getPos(self):
        return self.pos

    def getDimensions(self):
        return self.dimensions

    def getBoundingBox(self):
        return self.bBox

class ActionMark(Object):

    def __init__(self, x, y, dimX, dimY, action):
        Object.__init__(self, x, y, dimX, dimY)
        self.action = action
        return

    def getAction(self):
        return self.action

class TunnelObject(Object):

    def __init__(self, x, y, dimX, dimY, target, dropoffPoint, orient):
        Object.__init__(self, x, y, dimX, dimY)
        self.target = target
        self.dropoff = dropoffPoint
        self.orientation = orient # orient can be 0 for horizontal, 1 for vertical or 2 for absolute
        return

    def getTarget(self):
        return self.target

    def getDropoff(self):
        return self.dropoff

    def getOrientation(self):
        return self.orientation

class ObjectSprite(Object):

    def __init__(self, x, y, image, thickness):
        image = "../resrc/img/RPG/" + image + ".png"
        self.image = pygame.image.load(image).convert_alpha()
        dimX, dimY = self.image.get_width(), self.image.get_height()
        Object.__init__(self, x, y, dimX, dimY)
        self.thickness = thickness

        self.bBox = BoundingBox(x, y + dimY - thickness, x + dimX, y + dimY)
        return

    def getImage(self):
        return self.image

class Person(ObjectSprite):

    def __init__(self, x, y, image, thickness,  action):
        ObjectSprite.__init__(self, x, y, image, thickness)
        self.action = action
        return

    def getAction(self):
        return self.action


import pygame.image
from src.CommonModules.Constants import CollisionData
from src.CommonModules.Constants import Directions

class BoundingBox(object):

    def __init__(self, x1, y1, x2, y2):
        # why didn't I just use Rect class??! shoot me plz
        self.box = {"x1" : x1, "x2" : x2, "y1" : y1, "y2" : y2}
        return

    def updateBox(self, x1, y1, x2, y2):
        self.box = {"x1" : x1, "x2" : x2, "y1" : y1, "y2" : y2}

    def getCenter(self):
        y1, y2 = self.box["y1"], self.box["y2"]
        return y1+((y2-y1)/2)

    def getVertCenter(self):
        x1, x2 = self.box["x1"], self.box["x2"]
        return x1+((x2-x1)/2)

    def getBox(self):
        return self.box

    def collisionWithObject(self, direction, obj):
        objBox = obj.getBoundingBox().getBox()
        returnValue = {CollisionData.COLLISION : False,
                       CollisionData.POSITION : 0}

        # I want to punch myself in the face for writing this code...
        if      (  (self.box["x1"]+5 < objBox["x1"] and self.box["x2"]-5 > objBox["x1"])
                    or
                    (self.box["x1"]+5 < objBox["x2"] and self.box["x2"]-5 > objBox["x2"])
                    or
                    (
                        (self.box["x1"]+5 > objBox["x1"] and self.box["x2"]-5 > objBox["x1"])
                        and
                        (self.box["x1"]+5 < objBox["x2"] and self.box["x2"]-5 < objBox["x2"])
                    )):
            if direction == Directions.UP:
                if (self.box["y1"] <= objBox["y2"]) and (self.box["y2"]-5 > objBox["y1"]) :
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox["y2"]
                else:
                    returnValue[CollisionData.COLLISION] = False
            if direction == Directions.DOWN:
                if (self.box["y2"] >= objBox["y1"]) and (self.box["y1"]+5 < objBox["y2"]):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox["y1"]
                else:
                    returnValue[CollisionData.COLLISION] = False

        if      (  (self.box["y1"]+5 < objBox["y1"] and self.box["y2"]-5 > objBox["y1"])
                    or
                    (self.box["y1"]+5 < objBox["y2"] and self.box["y2"]-5 > objBox["y2"])
                    or
                    (
                        (self.box["y1"]+5 > objBox["y1"] and self.box["y2"]-5 > objBox["y1"])
                        and
                        (self.box["y1"]+5 < objBox["y2"] and self.box["y2"]-5 < objBox["y2"])
                    )):
            if direction == Directions.LEFT:
                if (self.box["x1"] <= objBox["x2"]) and (self.box["x2"]-5 > objBox["x1"]):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox["x2"]
                else:
                    returnValue[CollisionData.COLLISION] = False
            if direction == Directions.RIGHT:
                if (self.box["x2"] >= objBox["x1"]) and (self.box["x1"]+5 < objBox["x2"]):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox["x1"]
                else:
                    returnValue[CollisionData.COLLISION] = False
        return returnValue

    def collisionWithSceneBoundaries(self, direction, bound):
        if direction == Directions.UP:
            if self.box["y1"] <= bound:
                return True
            else:
                return False
        if direction == Directions.DOWN:
            if self.box["y2"] >= bound:
                return True
            else:
                return False
        if direction == Directions.LEFT:
            if self.box["x1"] <= bound:
                return True
            else:
                return False
        if direction == Directions.RIGHT:
            if self.box["x2"] >= bound:
                return True
            else:
                return False
        return

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

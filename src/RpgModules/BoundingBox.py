
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
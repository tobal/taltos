
from pygame import Rect
from CommonModules.Constants import CollisionData
from CommonModules.Constants import Directions

class BoundingBox(object):

    def __init__(self, x1, y1, x2, y2):
        self.box = Rect(x1, y1, x2-x1, y2-y1)
        return

    def updateBox(self, x1, y1, x2, y2):
        self.box = Rect(x1, y1, x2-x1, y2-y1)

    def getHorizontalCenter(self):
        return self.box.centery

    def getVerticalCenter(self):
        return self.box.centerx

    def getBox(self):
        return self.box

    def collisionWithObject(self, direction, obj):
        objBox = obj.getBoundingBox().getBox()
        returnValue = {CollisionData.COLLISION : False,
                       CollisionData.POSITION : 0}

        # I want to punch myself in the face for writing this code...
        if      (  (self.box.left+5 < objBox.left and self.box.right-5 > objBox.left)
                    or
                    (self.box.left+5 < objBox.right and self.box.right-5 > objBox.right)
                    or
                    (
                        (self.box.left+5 > objBox.left and self.box.right-5 > objBox.left)
                        and
                        (self.box.left+5 < objBox.right and self.box.right-5 < objBox.right)
                    )):
            if direction == Directions.UP:
                if (self.box.top <= objBox.bottom) and (self.box.bottom-5 > objBox.top) :
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox.bottom
                else:
                    returnValue[CollisionData.COLLISION] = False
            if direction == Directions.DOWN:
                if (self.box.bottom >= objBox.top) and (self.box.top+5 < objBox.bottom):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox.top
                else:
                    returnValue[CollisionData.COLLISION] = False

        if      (  (self.box.top+5 < objBox.top and self.box.bottom-5 > objBox.top)
                    or
                    (self.box.top+5 < objBox.bottom and self.box.bottom-5 > objBox.bottom)
                    or
                    (
                        (self.box.top+5 > objBox.top and self.box.bottom-5 > objBox.top)
                        and
                        (self.box.top+5 < objBox.bottom and self.box.bottom-5 < objBox.bottom)
                    )):
            if direction == Directions.LEFT:
                if (self.box.left <= objBox.right) and (self.box.right-5 > objBox.left):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox.right
                else:
                    returnValue[CollisionData.COLLISION] = False
            if direction == Directions.RIGHT:
                if (self.box.right >= objBox.left) and (self.box.left+5 < objBox.right):
                    returnValue[CollisionData.COLLISION] = True
                    returnValue[CollisionData.POSITION] = objBox.left
                else:
                    returnValue[CollisionData.COLLISION] = False
        return returnValue

    def collisionWithSceneBoundaries(self, direction, bound):
        if direction == Directions.UP:
            if self.box.top <= bound:
                return True
            else:
                return False
        if direction == Directions.DOWN:
            if self.box.bottom >= bound:
                return True
            else:
                return False
        if direction == Directions.LEFT:
            if self.box.left <= bound:
                return True
            else:
                return False
        if direction == Directions.RIGHT:
            if self.box.right >= bound:
                return True
            else:
                return False
        return

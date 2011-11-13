
import pygame
from pygame.locals import *
from src.CommonModules.Constants import Directions
from src.RpgModules.Objects import BoundingBox
from src.RpgModules.Images import BulcsuAnimation

class ProtagonistSprite(object):

    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.loadSprites()
        self.bBox = BoundingBox(self.posX, self.posY + 200, self.posX + 81, self.posY + 232)
        return
    
    def loadSprites(self):
        self.sprite = BulcsuAnimation.BulcsuAnimation()
        self.currentSprite = self.sprite.getAnimationFrame(Directions.RIGHT, 0)

    def getCurrentSprite(self):
        return self.currentSprite

    def go(self, direction):
        animation = self.sprite.getAnimation(direction)
        spritenum = len(animation)-1
        if self.currentSprite in animation:
            if animation.index(self.currentSprite) >= spritenum:
                self.currentSprite = self.sprite.getAnimationFrame(direction, 1)
            else:
                self.currentSprite = animation[animation.index(self.currentSprite)+1]
        else:
            self.currentSprite = self.sprite.getAnimationFrame(direction, 1)

    def stop(self, direction):
        self.currentSprite = self.sprite.getAnimationFrame(direction, 0)

    # axis has to be x or y
    def addToPos(self, axis, move):
        if axis == "x":
            self.posX += move
        elif axis == "y":
            self.posY += move

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getBoundingBox(self):
        self.bBox.updateBox(self.posX, self.posY + 200, self.posX + 81, self.posY + 232)
        return self.bBox

    def setPosX(self, x):
        self.posX = x

    def setPosY(self, y):
        self.posY = y

    def setPos(self, point):
        self.posX = point[0]
        self.posY = point[1]

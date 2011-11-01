import pygame
from pygame.locals import *
from Objects import BoundingBox

class ProtagonistSprite(object):

    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.loadSprites()
        self.bBox = BoundingBox(self.posX, self.posY + 200, self.posX + 81, self.posY + 232)
        return

    def loadImage(self,  imageName,  alpha):
        imagePath = "../resrc/img/RPG/" + imageName + ".png"
        if alpha:
            img = pygame.image.load(imagePath).convert_alpha()
        else:
            img = pygame.image.load(imagePath).convert()
        return img

    def loadSprites(self):
        lRightstand = [ self.loadImage("jobbraall",  True) ]
        lRightwalk = []
        for x in range(1, 7):
            lRightwalk.append(self.loadImage("jobbralep" + str(x),  True))

        lLeftstand = [ self.loadImage("balraall", True) ]
        lLeftwalk = []
        for x in range(1, 7):
            lLeftwalk.append(self.loadImage("balralep" + str(x), True))

        lBackstand = [ self.loadImage("hattalall",  True) ]
        lBackwalk = [ self.loadImage("hattallep1",  True),
                            self.loadImage("hattalall",  True),
                            self.loadImage("hattallep2",  True),
                            self.loadImage("hattalall",  True) ]

        lFrontstand = [ self.loadImage("szembenall",  True) ]
        lFrontwalk = [ self.loadImage("szembenlep1",  True),
                            self.loadImage("szembenlep2",  True),
                            self.loadImage("szembenlep3",  True),
                            self.loadImage("szembenlep2",  True) ]

        self.sprite = {"rightstand" : lRightstand,
                                "rightwalk" : lRightwalk,
                                "leftstand" : lLeftstand,
                                "leftwalk" : lLeftwalk,
                                "backstand" : lBackstand,
                                "backwalk" : lBackwalk,
                                "frontstand" : lFrontstand,
                                "frontwalk" : lFrontwalk}

        self.currentSprite = self.sprite["rightstand"][0]

    def getCurrentSprite(self):
        return self.currentSprite

    def going(self, str, spritenum):
        if self.currentSprite in self.sprite[str]:
            if self.sprite[str].index(self.currentSprite) >= spritenum-1:
                self.currentSprite = self.sprite[str][0]
            else:
                self.currentSprite = self.sprite[str][self.sprite[str].index(self.currentSprite)+1]
        else:
            self.currentSprite = self.sprite[str][0]

    def goRight(self):
        self.going("rightwalk", 6)
        return

    def goLeft(self):
        self.going("leftwalk", 6)
        return

    def goUp(self):
        self.going("backwalk", 4)
        return

    def goDown(self):
        self.going("frontwalk", 4)
        return

    def stopRight(self):
        self.currentSprite = self.sprite["rightstand"][0]

    def stopLeft(self):
        self.currentSprite = self.sprite["leftstand"][0]

    def stopUp(self):
        self.currentSprite = self.sprite["backstand"][0]

    def stopDown(self):
        self.currentSprite = self.sprite["frontstand"][0]

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

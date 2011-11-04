
import pygame.image
from pygame import Rect
from src.CommonModules.Constants import Directions
from src.CommonModules.Constants import DrawingOrder

class Scene(object):

    def __init__(self, name, image, bounds, tram):
        self.image = image
        self.bounds = {Directions.UP : bounds.top,
                       Directions.DOWN : bounds.bottom,
                       Directions.LEFT : bounds.left,
                       Directions.RIGHT : bounds.right}
        self.backGround = pygame.image.load(image).convert()
        self.tram = tram
        self.objects = []
        self.persons = []
        self.actionPoints = []
        self.tunnels = []
        self.name = name

    def isThereTram(self):
        return self.tram

    def addObject(self, object):
        self.objects.append(object)

    def addActionPoint(self, object):
        self.actionPoints.append(object)

    def addPerson(self, object):
        self.persons.append(object)

    def addTunnel(self, object):
        self.tunnels.append(object)

    def getObjects(self):
        return self.objects

    def getPersons(self):
        return self.persons

    def getActionPoints(self):
        return self.actionPoints

    def getTunnels(self):
        return self.tunnels

    def getBackGround(self):
        return self.backGround

    def getBounds(self):
        return self.bounds

    def getName(self):
        return self.name

    def drawBackGround(self, screen):
        screen.blit(self.backGround, (0,0))

    def drawObjects(self, order, spritePosY, screen):
        if order == DrawingOrder.FRONT:
            for obj in self.objects:
                if spritePosY < obj.getBoundingBox().getCenter():
                    screen.blit(obj.getImage(), (obj.getPos()))
            for obj in self.persons:
                if spritePosY < obj.getBoundingBox().getCenter():
                    screen.blit(obj.getImage(), (obj.getPos()))
        if order == DrawingOrder.BACK:
            for obj in self.objects:
                if spritePosY >= obj.getBoundingBox().getCenter():
                    screen.blit(obj.getImage(), (obj.getPos()))
            for obj in self.persons:
                if spritePosY >= obj.getBoundingBox().getCenter():
                    screen.blit(obj.getImage(), (obj.getPos()))
        return


import pygame
import random
from RpgModules.Images import RpgImages

class Tram(object):

    def __init__(self):
        self.timer = 0
        self.drawing = False
        self.speed = 20.0
        self.altitude = 10
        self.pos = -2846.0
        self.minTime = 400
        self.maxTime = 1000
        self.due = random.randint(self.minTime, self.maxTime)
        self.villamos = pygame.image.load(RpgImages.RpgImages.TRAM).convert_alpha()
        return

    def loop(self):
        if not(self.drawing):
            self.timer += 1
            if self.timer > self.due:
                self.pos = -2846.0
                self.drawing = True
        else:
            self.pos += self.speed
            if self.pos >= 1024:
                self.drawing = False
                self.timer = 0
                self.due = random.randint(self.minTime, self.maxTime)
        return

    def draw(self, screen):
        if self.drawing:
            screen.blit(self.villamos, (self.pos, self.altitude))
        return

    def modifyPos(self, value):
        self.pos += value
        return


import pygame
from pygame.locals import *
import MainExceptions

class KeyEventHandler(object):

    def __init__(self):
        pass

    def leftKeyUp(self):
        pass

    def rightKeyUp(self):
        pass

    def upKeyUp(self):
        pass

    def downKeyUp(self):
        pass

    def leftKeyDown(self):
        pass

    def rightKeyDown(self):
        pass

    def upKeyDown(self):
        pass

    def downKeyDown(self):
        pass

    def escape(self):
        raise MainExceptions.Exit()

    def enter(self):
        pass

    def postAction(self):
        pass

    def handleKeyEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.escape()
            if event.type == KEYDOWN:
                if (event.key == K_a) or (event.key == K_LEFT):
                    self.leftKeyDown()
                if (event.key == K_d) or (event.key == K_RIGHT):
                    self.rightKeyDown()
                if (event.key == K_w) or (event.key == K_UP):
                    self.upKeyDown()
                if (event.key == K_s) or (event.key == K_DOWN):
                    self.downKeyDown()
                if (event.key == K_q) or (event.key == K_ESCAPE):
                    self.escape()
                if (event.key == K_e) or (event.key == K_RETURN):
                    self.enter()
            if event.type == KEYUP:
                if (event.key == K_a) or (event.key == K_LEFT):
                    self.leftKeyUp()
                if (event.key == K_d) or (event.key == K_RIGHT):
                    self.rightKeyUp()
                if (event.key == K_w) or (event.key == K_UP):
                    self.upKeyUp()
                if (event.key == K_s) or (event.key == K_DOWN):
                    self.downKeyUp()

        self.postAction()



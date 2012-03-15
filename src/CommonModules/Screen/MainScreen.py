
import pygame
from pygame.constants import *
from CommonModules.Constants import GameModes

class MainScreen(object):

    def __init__(self):
        self.screen = 0
        self.resolution = [1024, 768]
        return

    def destroyScreen(self):
        pygame.display.quit()

    def getScreen(self):
        return self.screen

    def getResolution(self):
        return self.resolution

    def setScreenMode(self, gameMode):
        if gameMode == GameModes.RPG:
            self.screen = pygame.display.set_mode(self.resolution, FULLSCREEN, 32)
            pygame.mouse.set_visible(False)
        if gameMode == GameModes.CYBERSPACE:
            self.screen = pygame.display.set_mode(self.resolution, HWSURFACE|OPENGL|DOUBLEBUF|FULLSCREEN, 16)
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)
        pygame.display.set_caption("Taltos")

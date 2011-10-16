
import pygame
from pygame.constants import FULLSCREEN
from pygame.constants import RESIZABLE

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

    def createScreen(self):
        self.screen = pygame.display.set_mode(self.resolution, RESIZABLE, 32)
        pygame.display.set_caption("Taltos")
        pygame.mouse.set_visible(False)

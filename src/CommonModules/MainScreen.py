
import pygame
from pygame.constants import FULLSCREEN
from pygame.constants import RESIZABLE

class MainScreen():
    
    def __init__(self):
        self.screen = 0
        return
    
    def destroyScreen(self):
        pygame.display.quit()
    
    def getScreen(self):
        return self.screen

    def createScreen(self):
        resolution = [1024, 768]
        self.screen = pygame.display.set_mode(resolution, RESIZABLE, 32)
        pygame.display.set_caption("Taltos")
        pygame.mouse.set_visible(False)

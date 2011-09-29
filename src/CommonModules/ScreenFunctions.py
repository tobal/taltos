
import pygame
from pygame.constants import FULLSCREEN

def createScreen():
    resolution = [1024, 768]
    screen = pygame.display.set_mode(resolution, FULLSCREEN, 32)
    pygame.display.set_caption("Taltos")
    pygame.mouse.set_visible(False)
    return screen

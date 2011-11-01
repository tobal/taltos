
import pygame
from sys import exit
from pygame.time import Clock
import MainExceptions
from src.RpgModules import Rpg
from src.CommonModules.Screen import MainScreen
from src.CommonModules import MusicPlayer
from src.CommonModules import Menu

def setupScreen():
    gameScreen = MainScreen.MainScreen()
    gameScreen.createScreen()
    return gameScreen

pygame.init()

MusicPlayer.MusicPlayer().playContinously()
gameScreen = setupScreen()

language = Menu.Menu(gameScreen.getScreen()).languageChooser()
rpg = Rpg.Rpg(gameScreen.getScreen(), gameScreen.getResolution(), language)

# game loop
while True:
    clock = Clock()
    
    try:
        clock.tick(30)
        rpg.gameLoop()
    except MainExceptions.Exit:
        exit()

    pygame.display.update()

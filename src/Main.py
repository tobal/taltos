
import pygame
from sys import exit
from pygame.time import Clock
import MainExceptions
from RpgModules import Rpg
from CyberspaceModules import Cyberspace
from CommonModules.Screen import MainScreen
from CommonModules import MusicPlayer
from CommonModules import Menu
from CommonModules.Constants import GameModes

def initScreen():
    gameScreen = MainScreen.MainScreen()
    #gameScreen.setScreenMode(GameModes.RPG)
    gameScreen.setScreenMode(GameModes.CYBERSPACE)
    return gameScreen

pygame.init()

MusicPlayer.MusicPlayer().playContinously()
gameScreen = initScreen()

#language = Menu.Menu(gameScreen.getScreen()).languageChooser()
#rpg = Rpg.Rpg(gameScreen.getScreen(), language)
cyberspace = Cyberspace.Cyberspace()

# game loop
while True:
    clock = Clock()

    try:
        #clock.tick(30)
        #rpg.gameLoop()
        cyberspace.run()
    except MainExceptions.Exit:
        exit()

    #pygame.display.update()


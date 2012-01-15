
import pygame
from sys import exit
from pygame.time import Clock
import MainExceptions
from RpgModules import Rpg
from CyberspaceModules import Cyberspace
from CommonModules.Screen import MainScreen
from CommonModules import MusicPlayer
from CommonModules import Menu
from CommonModules import GameMode
from CommonModules.Constants import GameModes

def initGameMode(gameMode):
    gameMode = GameMode.GameMode(GameModes.RPG)
    return gameMode

def initScreen(gameMode):
    gameScreen = MainScreen.MainScreen()
    gameScreen.setScreenMode(gameMode)
    return gameScreen

pygame.init()
gameMode = initGameMode(GameModes.RPG)
gameScreen = initScreen(gameMode.getGameMode())

MusicPlayer.MusicPlayer().playContinously()
language = Menu.Menu(gameScreen.getScreen()).languageChooser()
rpg = Rpg.Rpg(gameScreen.getScreen(), language)
#cyberspace = Cyberspace.Cyberspace()

# game loop
while True:
    clock = Clock()

    try:
        clock.tick(30)
        rpg.handleKeyEvents()
        rpg.gameLoop()
        #cyberspace.run()
    except MainExceptions.Exit:
        exit()

    pygame.display.update()


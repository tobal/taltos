
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
    gameMode = GameMode.GameMode(gameMode)
    return gameMode

def initScreen(gameMode):
    gameScreen = MainScreen.MainScreen()
    gameScreen.setScreenMode(gameMode)
    return gameScreen

pygame.init()
gameMode = initGameMode(GameModes.RPG)
gameScreen = initScreen(GameModes.RPG)

MusicPlayer.MusicPlayer().playContinously()
language = Menu.Menu(gameScreen.getScreen()).languageChooser()
clock = Clock()

if gameMode.getGameMode() == GameModes.RPG:
    currentGameModule = Rpg.Rpg(gameScreen, language)
if gameMode.getGameMode() == GameModes.CYBERSPACE:
    gameScreen = initScreen(GameModes.CYBERSPACE)
    currentGameModule = Cyberspace.Cyberspace(gameScreen, language)

# game loop
while True:
    try:
        clock.tick(30)
        currentGameModule.handleKeyEvents()
        currentGameModule.gameLoop()
    except MainExceptions.Exit:
        exit()

    if gameMode.getGameMode() == GameModes.RPG:
        pygame.display.update()
    if gameMode.getGameMode() == GameModes.CYBERSPACE:
        pygame.display.flip()


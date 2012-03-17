
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

class TaltosGame():

    def __init__(self):
        pygame.init()
        self.clock = Clock()
        MusicPlayer.MusicPlayer().playContinously()

        self.gameMode = GameMode.GameMode(GameModes.RPG)
        self.gameScreen = MainScreen.MainScreen()
        self.gameScreen.setScreenMode(self.gameMode.getGameMode())
        self.language = Menu.Menu(self.gameScreen.getScreen()).languageChooser()

        """
        self.gameModules = {
                GameModes.RPG : None,
                GameModes.CYBERSPACE : None }
        """
        self.changeGameMode(GameModes.RPG)

    def changeGameMode(self, newGameMode):
        self.gameMode.setGameMode(newGameMode)
        self.gameScreen.setScreenMode(self.gameMode.getGameMode())
        if self.gameMode.getGameMode() == GameModes.RPG:
            self.currentGameModule = Rpg.Rpg(self.gameScreen, self.language)
        if self.gameMode.getGameMode() == GameModes.CYBERSPACE:
            self.currentGameModule = Cyberspace.Cyberspace(self.gameScreen, self.language)
        """
        if self.gameMode.getGameMode() == GameModes.RPG:
            if self.gameModules[GameModes.RPG] is None:
                self.gameModules[GameModes.RPG] = Rpg.Rpg(self.gameScreen, self.language)
        if self.gameMode.getGameMode() == GameModes.CYBERSPACE:
            if self.gameModules[GameModes.CYBERSPACE] is None:
                self.gameModules[GameModes.CYBERSPACE] = Cyberspace.Cyberspace(self.gameScreen, self.language)
        self.currentGameModule = self.gameModules[self.gameMode.getGameMode()]
        """

    def gameLoop(self):
        while True:
            try:
                self.clock.tick(30)
                self.currentGameModule.handleKeyEvents()
                self.currentGameModule.gameLoop()
            except MainExceptions.Exit:
                exit()
            except MainExceptions.ChangeGameMode as gameModeChange:
                self.changeGameMode(gameModeChange.newGameMode)

            if self.gameMode.getGameMode() == GameModes.RPG:
                pygame.display.update()
            if self.gameMode.getGameMode() == GameModes.CYBERSPACE:
                pygame.display.flip()

game = TaltosGame()
game.gameLoop()


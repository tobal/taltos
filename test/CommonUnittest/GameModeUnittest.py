
import unittest
from src.CommonModules.GameMode import GameMode
from src.CommonModules.Constants import gameModes

class GameModeUnittest(unittest.TestCase):
    
    def setUp(self):
        self.gamemode = GameMode()

    def tearDown(self):
        return

    def test_gamemode_is_rpg_on_init(self):
        self.assertTrue(self.gamemode.getGameMode() == gameModes.RPG, 
                        "Gamemode initialization error")
        
    def test_gamemode_handling(self):
        self.gamemode.setGameMode(gameModes.HACKING)
        self.assertTrue(self.gamemode.getGameMode() == gameModes.HACKING, 
                        "setGameMode doesn't work")
        self.gamemode.setGameMode(gameModes.CYBERSPACE)
        self.assertTrue(self.gamemode.getGameMode() == gameModes.CYBERSPACE, 
                        "setGameMode doesn't work")
        self.gamemode.setGameMode(gameModes.WORKSHOP)
        self.assertTrue(self.gamemode.getGameMode() == gameModes.WORKSHOP, 
                        "setGameMode doesn't work")

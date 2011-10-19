
import unittest
from src.CommonModules.GameMode import GameMode
from src.CommonModules.Constants import GameModes

class GameModeUnittest(unittest.TestCase):
    
    def setUp(self):
        self.gamemode = GameMode()

    def tearDown(self):
        return

    def test_gamemode_is_rpg_on_init(self):
        self.assertTrue(self.gamemode.getGameMode() == GameModes.RPG, 
                        "Gamemode initialization error")
        
    def test_gamemode_handling(self):
        self.gamemode.setGameMode(GameModes.HACKING)
        self.assertTrue(self.gamemode.getGameMode() == GameModes.HACKING, 
                        "setGameMode doesn't work")
        self.gamemode.setGameMode(GameModes.CYBERSPACE)
        self.assertTrue(self.gamemode.getGameMode() == GameModes.CYBERSPACE, 
                        "setGameMode doesn't work")
        self.gamemode.setGameMode(GameModes.WORKSHOP)
        self.assertTrue(self.gamemode.getGameMode() == GameModes.WORKSHOP, 
                        "setGameMode doesn't work")

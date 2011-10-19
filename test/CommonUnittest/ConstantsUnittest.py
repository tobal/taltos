
import unittest
from src.CommonModules.Constants import *

class ConstantsUnittest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_proper_bgcolor_got(self):
        white = (255,255,255)
        rpgmode = GameModes.RPG
        self.assertTrue(Colors.getBackgroundColor(Colors(), rpgmode) == white, "RPG background color is not white")

    def test_proper_fgcolor_got(self):
        grey = (100,100,100)
        rpgmode = GameModes.RPG
        self.assertTrue(Colors.getForegroundColor(Colors(), rpgmode) == grey, "RPG foreground color is not grey")
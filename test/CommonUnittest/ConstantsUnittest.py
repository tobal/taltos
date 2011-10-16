
import unittest
from src.CommonModules.Constants import *

class ConstantsUnittest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_proper_bgcolor_got(self):
        white = (255,255,255)
        rpgmode = gameModes.RPG
        self.assertTrue(colors.getBackgroundColor(rpgmode) == white, "RPG background color is not white")

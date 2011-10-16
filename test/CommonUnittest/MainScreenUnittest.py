
import unittest
from src.CommonModules.Screen import MainScreen
import pygame

class MainScreenUnittest(unittest.TestCase):

    def setUp(self):
        self.mainScreen = MainScreen.MainScreen()

    def tearDown(self):
        self.mainScreen.destroyScreen()

    def test_screen_init(self):
        self.assertTrue(self.mainScreen.getScreen() == 0, "Screen doesn't init")
    
    def test_screen_creation(self):
        self.mainScreen.createScreen()
        self.assertTrue(pygame.display.get_init(), "Screen not initialized properly")

    def test_proper_resolution(self):
        rightRes = [1024,768]
        resolution = self.mainScreen.getResolution()
        self.assert_(resolution == rightRes, "Improper resolution")
        
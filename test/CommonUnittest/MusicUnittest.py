import unittest
from src.CommonModules import MusicPlayer
import pygame

class MusicUnittest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_plays_continuously(self):
        musicPlayer = MusicPlayer.MusicPlayer()
        musicPlayer.playContinously()
        assert pygame.mixer.get_init()

#if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
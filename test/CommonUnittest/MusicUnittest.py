import unittest
from src.CommonModules import MusicPlayer
import pygame

class MusicUnittest(unittest.TestCase):

    def setUp(self):
        self.musicPlayer = MusicPlayer.MusicPlayer()

    def tearDown(self):
        self.musicPlayer.stopMusic()

    def test_continuous_play(self):
        self.musicPlayer.playContinously()
        self.assertTrue(pygame.mixer.get_init(), "Mixer doesn't init")
        #self.assertTrue(pygame.mixer.get_busy(), "Music doesn't play") 

    def test_stoping_play(self):
        self.musicPlayer.stopMusic()
        self.assertFalse(pygame.mixer.get_busy(), "Music doesn't stop")
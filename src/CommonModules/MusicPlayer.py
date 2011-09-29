
from pygame import mixer

class MusicPlayer(object):

    def __init__(self,selfparams):
        mixer.pre_init(44100, -16, 2, 1024*4)

    def playContinously(self):
        mixer.music.load("../resrc/music/tantra_people.ogg")
        mixer.music.play(-1)

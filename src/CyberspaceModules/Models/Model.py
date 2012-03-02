
from CyberspaceModules.Geoms.UVVector import UVVector

class Model(object):
    UV0 = [
            UVVector(0,0),
            UVVector(1,0),
            UVVector(1,1),
            UVVector(0,1)
    ]
    UV90 = [
            UVVector(0,1),
            UVVector(0,0),
            UVVector(1,0),
            UVVector(1,1)
    ]
    UV180 = [
            UVVector(1,1),
            UVVector(0,1),
            UVVector(0,0),
            UVVector(1,0)
    ]
    UV270 = [
            UVVector(1,0),
            UVVector(1,1),
            UVVector(0,1),
            UVVector(0,0)
    ]

    def __init__(self):
        self.UVVectors = []
        self.Vectors = []
        self.Lines = []
        self.Textures = []
        self.TextureIndexes = []

    def getUVVectors(self):
        return self.UVVectors

    def getVectors(self):
        return self.Vectors

    def getLines(self):
        return self.Lines

    def getTextures(self):
        return self.Textures

    def getTextureIndexes(self):
        return self.TextureIndexes

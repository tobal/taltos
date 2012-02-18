
class Model(object):
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

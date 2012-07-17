
from CyberspaceModules.Vrml import Grid
from CyberspaceModules.Vrml import Structure

class VrmlFile(object):
    def __init__(self, name):
        self.name = name
        self.grid = Grid(10, 40)
        self.structures = [Structure]

    def setGrid(self, nrOfQuads, sizeOfQuad):
        self.grid.nrOfQuads = nrOfQuads
        self.grid.sizeOfQuad = sizeOfQuad

    def addStructure(self, model):
        self.structures.append(model)


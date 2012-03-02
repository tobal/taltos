
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from CommonModules.Screen.ImageHandler import ImageHandler
from CommonModules.Constants import Models
from CyberspaceModules.Geoms.Vertex import Vertex
from CyberspaceModules.Geoms.Quad import Quad
from CyberspaceModules.Mesh.Mesh import Mesh
from CyberspaceModules.Mesh.Face import Face

from CyberspaceModules.Models.SmallHouse import SmallHouse

class MeshLoader():
    def __init__(self):
        self.model = None

    def loadTextures(self, model):
        Textures = model.getTextures()
        textures = glGenTextures(len(Textures))
        for textureId in range(len(Textures)):
            textureSurface = ImageHandler().loadImage(Textures[textureId])
            textureData = pygame.image.tostring(textureSurface, "RGB", True)
            glBindTexture(GL_TEXTURE_2D, textures[textureId])
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
            width, height = textureSurface.get_rect().size
            gluBuild2DMipmaps(GL_TEXTURE_2D, 3,
                    width, height,
                    GL_RGB, GL_UNSIGNED_BYTE, textureData)
        return textures

    def getVertices(self, vectors, vectorIndex, model):
        vectorQuad = vectors[vectorIndex]
        uvVectors = model.getUVVectors()
        uvVector = uvVectors[vectorIndex]

        vertices = []
        for i in range(4):
            vertex = Vertex(vectorQuad[i], uvVector[i])
            vertices.append(vertex)
        return vertices

    def getQuads(self, model):
        vectors = model.getVectors()
        quads = []
        numVectors = vectors.__len__()
        for vectorIndex in range(numVectors):
            vertices = self.getVertices(vectors, vectorIndex, model)
            quad = Quad(vertices)
            quads.append(quad)
        return quads

    def getFaces(self, model):
        textureIndexes = model.getTextureIndexes()
        quads = self.getQuads(model)
        faces = []
        for quadIndex in range(len(quads)):
            face = Face(textureIndexes[quadIndex], quads[quadIndex])
            faces.append(face)
        return faces

    def getModel(self, model):
        if model == Models.SMALLHOUSE:
            return SmallHouse()

    def getMesh(self, model):
        model = self.getModel(model)
        mesh = Mesh()
        mesh.faces = self.getFaces(model)
        mesh.lines = model.getLines()
        mesh.textures = self.loadTextures(model)
        return mesh



import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from CommonModules.Screen.ImageHandler import ImageHandler
from CyberspaceModules.Geoms.Vector import Vector
from CyberspaceModules.Geoms.Vertex import Vertex
from CyberspaceModules.Geoms.Quad import Quad
from CyberspaceModules.Geoms.UVVector import UVVector
from CyberspaceModules.Mesh.Mesh import Mesh
from CyberspaceModules.Mesh.Face import Face

UVVectors = [
                UVVector(0,0),
                UVVector(1,0),
                UVVector(1,1),
                UVVector(0,1)
            ]

Vectors = [
            [ # front face
                Vector(0,0,0),
                Vector(1,0,0),
                Vector(1,1,0),
                Vector(0,1,0)
            ],
            [
                Vector(1,0,0),
                Vector(2,0,0),
                Vector(2,1,0),
                Vector(1,1,0)
            ],
            [
                Vector(2,0,0),
                Vector(3,0,0),
                Vector(3,1,0),
                Vector(2,1,0)
            ],
            [
                Vector(1,1,0),
                Vector(2,1,0),
                Vector(2,2,0),
                Vector(1,2,0)
            ],
            [ # right face
                Vector(3,0,0),
                Vector(3,0,1),
                Vector(3,1,1),
                Vector(3,1,0)
            ],
            [
                Vector(3,0,1),
                Vector(3,0,2),
                Vector(3,1,2),
                Vector(3,1,1)
            ],
            [
                Vector(3,0,2),
                Vector(3,0,3),
                Vector(3,1,3),
                Vector(3,1,2)
            ],
            [
                Vector(3,1,1),
                Vector(3,1,2),
                Vector(3,2,2),
                Vector(3,2,1)
            ],
            [ # left face
                Vector(0,0,1),
                Vector(0,0,0),
                Vector(0,1,0),
                Vector(0,1,1)
            ],
            [
                Vector(0,0,2),
                Vector(0,0,1),
                Vector(0,1,1),
                Vector(0,1,2)
            ],
            [
                Vector(0,0,3),
                Vector(0,0,2),
                Vector(0,1,2),
                Vector(0,1,3)
            ],
            [
                Vector(0,1,2),
                Vector(0,1,1),
                Vector(0,2,1),
                Vector(0,2,2)
            ],
            [ # back face
                Vector(3,0,3),
                Vector(2,0,3),
                Vector(2,1,3),
                Vector(3,1,3)
            ],
            [
                Vector(2,0,3),
                Vector(1,0,3),
                Vector(1,1,3),
                Vector(2,1,3)
            ],
            [
                Vector(1,0,3),
                Vector(0,0,3),
                Vector(0,1,3),
                Vector(1,1,3)
            ],
            [
                Vector(2,1,3),
                Vector(1,1,3),
                Vector(1,2,3),
                Vector(2,2,3)
            ],
            [ # front right corner
                Vector(3,1,0),
                Vector(3,1,1),
                Vector(2,1,1),
                Vector(2,1,0)
            ],
            [
                Vector(2,1,0),
                Vector(2,1,1),
                Vector(2,3,1),
                Vector(2,2,0)
            ],
            [
                Vector(2,1,1),
                Vector(3,1,1),
                Vector(3,2,1),
                Vector(2,3,1)
            ],
            [ # front left corner
                Vector(1,1,0),
                Vector(1,1,1),
                Vector(0,1,1),
                Vector(0,1,0)
            ],
            [
                Vector(1,1,0),
                Vector(1,2,0),
                Vector(1,3,1),
                Vector(1,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(1,1,1),
                Vector(1,3,1),
                Vector(0,2,1)
            ],
            [ # back right corner
                Vector(3,1,2),
                Vector(3,1,3),
                Vector(2,1,3),
                Vector(2,1,2)
            ],
            [
                Vector(3,1,2),
                Vector(2,1,2),
                Vector(2,3,2),
                Vector(3,2,2)
            ],
            [
                Vector(2,1,2),
                Vector(2,1,3),
                Vector(2,2,3),
                Vector(2,3,2)
            ],
            [ # back left corner
                Vector(1,1,2),
                Vector(1,1,3),
                Vector(0,1,3),
                Vector(0,1,2)
            ],
            [
                Vector(1,1,2),
                Vector(0,1,2),
                Vector(0,2,2),
                Vector(1,3,2)
            ],
            [
                Vector(1,1,3),
                Vector(1,1,2),
                Vector(1,3,2),
                Vector(1,2,3)
            ],
            [ # top face
                Vector(2,3,1),
                Vector(2,3,2),
                Vector(1,3,2),
                Vector(1,3,1)
            ],
            [
                Vector(1,2,0),
                Vector(2,2,0),
                Vector(2,3,1),
                Vector(1,3,1)
            ],
            [
                Vector(3,2,1),
                Vector(3,2,2),
                Vector(2,3,2),
                Vector(2,3,1)
            ],
            [
                Vector(0,2,2),
                Vector(0,2,1),
                Vector(1,3,1),
                Vector(1,3,2)
            ],
            [
                Vector(2,2,3),
                Vector(1,2,3),
                Vector(1,3,2),
                Vector(2,3,2)
            ]
        ]

Lines = [
            [ # front face
                Vector(0,0,0),
                Vector(0,1,0)
            ],
            [
                Vector(0,1,0),
                Vector(1,1,0)
            ],
            [
                Vector(0,0,0),
                Vector(3,0,0)
            ],
            [
                Vector(1,1,0),
                Vector(1,2,0)
            ],
            [
                Vector(1,2,0),
                Vector(2,2,0)
            ],
            [
                Vector(2,2,0),
                Vector(2,1,0)
            ],
            [
                Vector(2,1,0),
                Vector(3,1,0)
            ],
            [ # right face
                Vector(3,0,3),
                Vector(3,0,0)
            ],
            [
                Vector(3,0,0),
                Vector(3,1,0)
            ],
            [
                Vector(3,1,0),
                Vector(3,1,1)
            ],
            [
                Vector(3,1,1),
                Vector(3,2,1)
            ],
            [
                Vector(3,2,1),
                Vector(3,2,2)
            ],
            [
                Vector(3,2,2),
                Vector(3,1,2)
            ],
            [
                Vector(3,1,2),
                Vector(3,1,3)
            ],
            [ # left face
                Vector(0,0,0),
                Vector(0,0,3)
            ],
            [
                Vector(0,0,3),
                Vector(0,1,3)
            ],
            [
                Vector(0,1,3),
                Vector(0,1,2)
            ],
            [
                Vector(0,1,2),
                Vector(0,2,2)
            ],
            [
                Vector(0,2,2),
                Vector(0,2,1)
            ],
            [
                Vector(0,2,1),
                Vector(0,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(0,1,0)
            ],
            [ # back face
                Vector(0,0,3),
                Vector(3,0,3)
            ],
            [
                Vector(3,0,3),
                Vector(3,1,3)
            ],
            [
                Vector(3,1,3),
                Vector(2,1,3)
            ],
            [
                Vector(2,1,3),
                Vector(2,2,3)
            ],
            [
                Vector(2,2,3),
                Vector(1,2,3)
            ],
            [
                Vector(1,2,3),
                Vector(1,1,3)
            ],
            [
                Vector(1,1,3),
                Vector(0,1,3)
            ],
            [ # front right corner
                Vector(2,1,0),
                Vector(2,1,1)
            ],
            [
                Vector(2,1,1),
                Vector(2,3,1)
            ],
            [
                Vector(3,1,1),
                Vector(2,1,1)
            ],
            [ # front left corner
                Vector(1,1,0),
                Vector(1,1,1)
            ],
            [
                Vector(0,1,1),
                Vector(1,1,1)
            ],
            [
                Vector(1,1,1),
                Vector(1,3,1)
            ],
            [ # back right corner
                Vector(3,1,2),
                Vector(2,1,2)
            ],
            [
                Vector(2,1,3),
                Vector(2,1,2)
            ],
            [
                Vector(2,1,2),
                Vector(2,3,2)
            ],
            [ # back left corner
                Vector(0,1,2),
                Vector(1,1,2)
            ],
            [
                Vector(1,1,3),
                Vector(1,1,2)
            ],
            [
                Vector(1,1,2),
                Vector(1,3,2)
            ],
            [ # top face
                Vector(1,2,0),
                Vector(1,3,1)
            ],
            [
                Vector(2,2,0),
                Vector(2,3,1)
            ],
            [
                Vector(3,2,1),
                Vector(2,3,1)
            ],
            [
                Vector(3,2,2),
                Vector(2,3,2)
            ],
            [
                Vector(2,2,3),
                Vector(2,3,2)
            ],
            [
                Vector(1,2,3),
                Vector(1,3,2)
            ],
            [
                Vector(0,2,2),
                Vector(1,3,2)
            ],
            [
                Vector(0,2,1),
                Vector(1,3,1)
            ],
            [
                Vector(1,3,1),
                Vector(1,3,2)
            ],
            [
                Vector(1,3,2),
                Vector(2,3,2)
            ],
            [
                Vector(2,3,2),
                Vector(2,3,1)
            ],
            [
                Vector(2,3,1),
                Vector(1,3,1)
            ]
        ]

Textures = [
            "../Cyber/zold_negyzet",
            "../Cyber/zold_jobbszel",
            "../Cyber/zold_balszel",
            "../Cyber/zold_alsoszel",
            "../Cyber/zold_2sarok_fent"
           ]

TextureIndexes = [ 1,4,2,3, # front face
                1,4,2,3, # right face
                2,4,1,3, # left face
                1,4,2,3, # back face
                0,0,0, # front right corner
                0,0,0, # front left corner
                0,0,0, # back right corner
                0,0,0, # back left corner
                0,0,0,0,0 # top face
                ]

def loadTextures():
    textures = glGenTextures(len(Textures))
    for textureId in range(len(Textures)):
        textureSurface = ImageHandler().loadImage(Textures[textureId])
        textureData = pygame.image.tostring(textureSurface, "RGB", True)
        glBindTexture(GL_TEXTURE_2D, textures[textureId])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        width, height = textureSurface.get_rect().size
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3,
                width, height,
                GL_RGB, GL_UNSIGNED_BYTE, textureData)
    return textures

def getVertices(vectorQuad):
    vertices = []
    for i in range(4):
        vertex = Vertex(vectorQuad[i], UVVectors[i])
        vertices.append(vertex)
    return vertices

def getQuads():
    quads = []
    for vectorQuad in Vectors:
        vertices = getVertices(vectorQuad)
        quad = Quad(vertices)
        quads.append(quad)
    return quads

def getFaces():
    quads = getQuads()
    faces = []
    for quadIndex in range(len(quads)):
        face = Face(TextureIndexes[quadIndex], quads[quadIndex])
        faces.append(face)
    return faces

def getMesh():
    mesh = Mesh()
    mesh.faces = getFaces()
    mesh.lines = Lines
    mesh.textures = loadTextures()
    return mesh


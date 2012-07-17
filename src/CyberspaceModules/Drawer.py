
from OpenGL.GL import *

class Drawer(object):
    def __init__(self):
        pass

    def drawBaseGrid(self):
        glBindTexture(GL_TEXTURE_2D, 1)
        nrOfQuads = 10
        sizeOfQuad = 40
        size = nrOfQuads * sizeOfQuad
        camHeight = 10.0
        for gridX in range(-size, size, sizeOfQuad):
            for gridZ in range(-size, size, sizeOfQuad):
                glBegin(GL_QUADS)
                glTexCoord2f(0, 0)
                glVertex(gridX, -camHeight, gridZ)
                glTexCoord2f(1, 0)
                glVertex(gridX + sizeOfQuad, -camHeight, gridZ)
                glTexCoord2f(1, 1)
                glVertex(gridX + sizeOfQuad, -camHeight, gridZ + sizeOfQuad)
                glTexCoord2f(0, 1)
                glVertex(gridX, -camHeight, gridZ + sizeOfQuad)
                glEnd()

    def drawMesh(self):
        for face in self.mesh.faces:
            glBindTexture(GL_TEXTURE_2D, face.textureIndex)
            glBegin(GL_QUADS)
            for vertex in face.geom.vertices:
                glTexCoord2f(
                        vertex.uv.u,
                        vertex.uv.v)
                glVertex(
                        vertex.vector.x,
                        vertex.vector.y,
                        vertex.vector.z)
            glEnd()


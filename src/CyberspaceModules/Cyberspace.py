
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from CommonModules.GameModule import GameModule
from CommonModules.Constants import Models
from CommonModules.Constants import GameModes
from CyberspaceModules.Geoms.Vector import Vector
from CyberspaceModules.Mesh.MeshLoader import MeshLoader
from MainExceptions import ChangeGameMode

piover180 = 0.0174532925

class Cyberspace(GameModule):

    def __init__(self, gameScreen, language):
        GameModule.__init__(self, gameScreen, language)

        self.translation = Vector(0,0,0)
        self.position = Vector(0,0,0)
        self.rotation = Vector(0,0,0)
        self.rotSpeed = Vector(0,0,0)
        self.forward = 0
        self.backward = 0
        self.strafeLeft = 0
        self.strafeRight = 0
        self.moveSpeed = 2.0

        self.glInit()
        self.resize(gameScreen.getResolution())
        self.mesh = MeshLoader().getMesh(Models.SMALLHOUSE)

        self.displayList = None

    def glInit(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_TEXTURE_2D)

    def resize(self, resolution):
        width, height = resolution
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(width)/height, 1.0, 10000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def translateScene(self):
        heading = 360 - self.rotation.y
        if self.forward == 1:
            self.position.x -= sin(heading * piover180) * self.moveSpeed
            self.position.z -= cos(heading * piover180) * self.moveSpeed
        elif self.backward == 1:
            self.position.x += sin(heading * piover180) * self.moveSpeed
            self.position.z += cos(heading * piover180) * self.moveSpeed
        if self.strafeLeft == 1:
            self.position.x += sin((heading - 90) * piover180) * self.moveSpeed
            self.position.z += cos((heading - 90) * piover180) * self.moveSpeed
        elif self.strafeRight == 1:
            self.position.x += sin((heading + 90) * piover180) * self.moveSpeed
            self.position.z += cos((heading + 90) * piover180) * self.moveSpeed
        self.translation.x = -self.position.x
        self.translation.z = -self.position.z
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)

    def rotateScene(self):
        lookUpLimit = 90.0
        sensitivity = 6
        y, x = pygame.mouse.get_rel()
        self.rotation.x += x / sensitivity
        if self.rotation.x > lookUpLimit:
            self.rotation.x = lookUpLimit
        elif self.rotation.x < -lookUpLimit:
            self.rotation.x = -lookUpLimit
        self.rotation.y += (y / sensitivity) % 360
        glRotatef(self.rotation.x, 1.0, 0.0, 0.0)
        glRotatef(self.rotation.y, 0.0, 1.0, 0.0)

    def drawBaseGrid(self):
        """
        gridSize = 400
        gridInterval = 40
        camHeight = 10.0
        glLineWidth(4)
        glBegin(GL_LINE)
        glColor(0.0, 1.0, 0.0)
        for grid in range(-gridSize, gridSize, gridInterval):
            glVertex(grid, -camHeight, -gridSize)
            glVertex(grid, -camHeight, -gridSize + gridSize*2)
            glVertex(-gridSize, -camHeight, grid)
            glVertex(-gridSize + gridSize*2, -camHeight, grid)
        glEnd()
        """
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
        """
            glDisable(GL_TEXTURE_2D)
            glColor(0.0, 0.0, 0.0)
            for face in self.mesh.faces:
                glBegin(GL_QUADS)
                for vertex in face.geom.vertices:
                    glVertex(
                            vertex.vector.x,
                            vertex.vector.y,
                            vertex.vector.z)
                glEnd()
            glEnable(GL_TEXTURE_2D)
            glColor(0.0, 1.0, 0.0)
            for line in self.mesh.lines:
                glBegin(GL_LINE)
                for vector in line:
                    glVertex(vector.x,
                            vector.y,
                            vector.z)
                glEnd()
        """
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

    def draw(self):
        glLoadIdentity()
        self.rotateScene()
        self.translateScene()

        if self.displayList is None:
            self.displayList = glGenLists(1)
            glNewList(self.displayList, GL_COMPILE)

            self.drawBaseGrid()
            glTranslatef(-80,-10,-200)
            glScalef(40,40,40)
            self.drawMesh()
            glTranslatef(6,0,4)
            glScalef(0.5,0.5,0.5)
            self.drawMesh()
            glTranslatef(-10,0,15)
            glScalef(2,2,2)
            self.drawMesh()

            glEndList()
        else:
            glCallList(self.displayList)

    def leftKeyUp(self):
        self.strafeLeft = 0

    def rightKeyUp(self):
        self.strafeRight = 0

    def upKeyUp(self):
        self.forward = 0

    def downKeyUp(self):
        self.backward = 0

    def leftKeyDown(self):
        self.strafeLeft = 1

    def rightKeyDown(self):
        self.strafeRight = 1

    def upKeyDown(self):
        self.forward = 1

    def downKeyDown(self):
        self.backward = 1

    def enter(self):
        raise ChangeGameMode(GameModes.RPG)

    def postAction(self):
        pass

    def gameLoop(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw()


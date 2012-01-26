
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from CommonModules.GameModule import GameModule
from CommonModules.Screen.ImageHandler import ImageHandler
from CyberspaceModules.Geoms.Vector import Vector

piover180 = 0.0174532925

class Cyberspace(GameModule):

    def __init__(self, gameScreen, language):
        GameModule.__init__(self, gameScreen, language)

        self.translation = Vector()
        self.position = Vector()
        self.rotation = Vector()
        self.rotSpeed = Vector()
        self.forward = 0
        self.backward = 0
        self.strafeLeft = 0
        self.strafeRight = 0
        self.moveSpeed = 2.0

        self.glInit()
        self.resize(gameScreen.getResolution())
        self.loadTexture()

    def glInit(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_SMOOTH)
        #glEnable(GL_TEXTURE_2D)
        glEnable(GL_COLOR_MATERIAL)
        #glEnable(GL_LIGHTING)
        #glEnable(GL_LIGHT0)
        glEnable(GL_BLEND)
        glLight(GL_LIGHT0, GL_POSITION, (0, 1, 1, 0))

    def resize(self, resolution):
        width, height = resolution
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, float(width)/height, 1.0, 10000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def loadTexture(self):
        textureSurface = ImageHandler().loadImage("../Cyber/zold_negyzet")
        textureData = pygame.image.tostring(textureSurface, "RGB", True)
        self.texture = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        width, height = textureSurface.get_rect().size
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3,
                width, height,
                GL_RGB, GL_UNSIGNED_BYTE, textureData)

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
        gridSize = 400
        gridInterval = 40
        camHeight = 10.0
        glLineWidth(3)
        glBegin(GL_LINE)
        glColor(0.0, 1.0, 0.0)
        for grid in range(-gridSize, gridSize, gridInterval):
            glVertex(grid, -camHeight, -gridSize)
            glVertex(grid, -camHeight, -gridSize + gridSize*2)
            glVertex(-gridSize, -camHeight, grid)
            glVertex(-gridSize + gridSize*2, -camHeight, grid)
        glEnd()
        """
        nrOfQuads = 20
        sizeOfQuad = 20
        size = nrOfQuads * sizeOfQuad
        camHeight = 6.0
        for gridX in range(-size, size, sizeOfQuad):
            for gridZ in range(-size, size, sizeOfQuad):
                glBegin(GL_QUADS)
                glColor(0.0, 0.0, 0.0)
                glTexCoord2f(0, 1)
                glVertex(gridX, -camHeight, gridZ)
                glTexCoord2f(1, 1)
                glVertex(gridX + sizeOfQuad, -camHeight, gridZ)
                glTexCoord2f(1, 0)
                glVertex(gridX + sizeOfQuad, -camHeight, gridZ + sizeOfQuad)
                glTexCoord2f(0, 0)
                glVertex(gridX, -camHeight, gridZ + sizeOfQuad)
                glEnd()
        """

    def draw(self):
        glLoadIdentity()
        self.rotateScene()
        self.translateScene()
        self.drawBaseGrid()

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
        pass

    def postAction(self):
        pass

    def gameLoop(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw()


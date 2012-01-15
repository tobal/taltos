
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from CommonModules.GameModule import GameModule
from CommonModules.Screen.ImageHandler import ImageHandler

class Cyberspace(GameModule):

    def __init__(self, gameScreen, language):
        GameModule.__init__(self, gameScreen, language)
        self.glInit()
        self.resize(gameScreen.getResolution())
        self.loadTexture()

    def glInit(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
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

    def draw(self):
        for gridX in range(-400, 400, 4):
            for gridZ in range(-400, 400, 4):
                glBegin(GL_QUADS)
                #glColor(1.0, 0.0, 0.0)
                glTexCoord2f(0, 1)
                glVertex(gridX, -3.0, gridZ)
                glTexCoord2f(1, 1)
                glVertex(gridX+4, -3.0, gridZ)
                glTexCoord2f(1, 0)
                glVertex(gridX+4, -3.0, gridZ+4)
                glTexCoord2f(0, 0)
                glVertex(gridX, -3.0, gridZ+4)
                glEnd()

    def leftKeyUp(self):
        pass

    def rightKeyUp(self):
        pass

    def upKeyUp(self):
        pass

    def downKeyUp(self):
        pass

    def leftKeyDown(self):
        pass

    def rightKeyDown(self):
        pass

    def upKeyDown(self):
        pass

    def downKeyDown(self):
        pass

    def enter(self):
        pass

    def postAction(self):
        pass

    def gameLoop(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw()


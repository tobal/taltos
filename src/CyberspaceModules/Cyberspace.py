
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from CommonModules.GameModule import GameModule
from CommonModules.Screen.ImageHandler import ImageHandler

class Cyberspace(GameModule):

    def __init__(self, screen, language):
        GameModule.__init__(screen, language)
        self.init()
        self.resize(1024, 768)
        self.loadTexture()

    def init(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_FLAT)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLight(GL_LIGHT0, GL_POSITION, (0, 1, 1, 0))

    def resize(self, width, height):
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

    def run(self):
        #clock = pygame.time.Clock()
        while(True):
            """
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYUP and event.key == K_ESCAPE:
                    exit()

            time_passed = clock.tick()
            time_passed_seconds = time_passed / 1000
            """
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.draw()

            pygame.display.flip()


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Cyberspace(object):

    def __init__(self):
        self.init()
        self.resize(1024, 768)

    def init(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_FLAT)
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

    def draw(self):
        glBegin(GL_QUADS)
        glColor(1.0, 0.0, 0.0)
        glVertex(100.0, 100.0, -20.0)
        glVertex(200.0, 100.0, -20.0)
        glVertex(200.0, 200.0, -20.0)
        glVertex(100.0, 200.0, -20.0)
        glEnd()

    def run(self):
        clock = pygame.time.Clock()
        while(True):
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYUP and event.key == K_ESCAPE:
                    exit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            time_passed = clock.tick()
            time_passed_seconds = time_passed / 1000

            self.draw()

            pygame.display.flip()


from OpenGL.GL import *
from OpenGL.GLU import *

class Cyberspace(object):

    def __init__(self):
        pass
    
    def init(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(1.0, 1.0, 1.0, 0.0)
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
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class EnvironmentObject:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.size = 1

    def draw(self):
        pass

class Tree(EnvironmentObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 1, 0)
        glutSolidCone(self.size, self.size * 2, 20, 20)
        glPopMatrix()

class Rock(EnvironmentObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0.5, 0.5, 0.5)
        glutSolidSphere(self.size, 20, 20)
        glPopMatrix()

class Lake(EnvironmentObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.size = 5

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 0, 1)
        glBegin(GL_QUADS)
        glVertex3f(-self.size, 0, -self.size)
        glVertex3f(self.size, 0, -self.size)
        glVertex3f(self.size, 0, self.size)
        glVertex3f(-self.size, 0, self.size)
        glEnd()
        glPopMatrix()

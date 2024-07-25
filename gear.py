from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Gear:
    def __init__(self, x, y, z, name):
        self.position = [x, y, z]
        self.size = 0.5
        self.name = name

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 0, 1)
        glutSolidCube(self.size)
        glPopMatrix()

    def check_collision(self, player_pos):
        px, py, pz = player_pos
        ox, oy, oz = self.position
        distance = ((px - ox)**2 + (py - oy)**2 + (pz - oz)**2)**0.5
        if distance < self.size:
            return True
        return False

class Helmet(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Helmet')

class Headphones(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Headphones')

class ChestArmor(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Chest Armor')

class TacticalRig(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Tactical Rig')

class Gun(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Gun')

class Knife(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Knife')

class FaceMask(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Face Mask')

class Backpack(Gear):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 'Backpack')

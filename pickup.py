from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Pickup:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.size = 0.5

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 1, 0)
        glutSolidCube(self.size)
        glPopMatrix()

    def check_collision(self, player_pos):
        px, py, pz = player_pos
        ox, oy, oz = self.position
        distance = ((px - ox)**2 + (py - oy)**2 + (pz - oz)**2)**0.5
        if distance < self.size:
            return True
        return False

class HealthPickup(Pickup):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def apply_effect(self, player_health):
        player_health[0] = min(100, player_health[0] + 25)

class AmmoPickup(Pickup):
    def __init__(self, x, y, z, ammo_type):
        super().__init__(x, y, z)
        self.ammo_type = ammo_type

    def apply_effect(self, inventory):
        inventory.add_ammo(self.ammo_type, 10)

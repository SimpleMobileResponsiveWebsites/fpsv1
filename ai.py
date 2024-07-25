from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

class AI:
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.size = 1

    def update(self, player_pos, player_health):
        # Basic AI behavior: move towards the player
        direction = [
            player_pos[0] - self.position[0],
            player_pos[1] - self.position[1],
            player_pos[2] - self.position[2]
        ]
        length = (direction[0]**2 + direction[1]**2 + direction[2]**2)**0.5
        if length > 0:
            direction = [d / length for d in direction]
            speed = 0.05
            self.position = [self.position[i] + direction[i] * speed for i in range(3)]

        # Basic attack: reduce player health if close enough
        distance = ((self.position[0] - player_pos[0])**2 + (self.position[1] - player_pos[1])**2 + (self.position[2] - player_pos[2])**2)**0.5
        if distance < self.size:
            player_health[0] -= 0.1

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(1, 0, 0)
        glutSolidSphere(self.size, 20, 20)
        glPopMatrix()

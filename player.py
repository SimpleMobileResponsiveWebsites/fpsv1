import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def handle_keys(player_pos, player_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[2] += player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[2] -= player_speed

def draw_player(player_pos):
    glPushMatrix()
    glTranslatef(*player_pos)
    glColor3f(1, 0, 0)
    glutSolidCube(1)
    glPopMatrix()

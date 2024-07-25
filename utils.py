import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def display_inventory(screen, inventory):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Health: {inventory.health}', True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    for i, gear in enumerate(inventory.gear):
        text_surface = font.render(gear.name, True, (255, 255, 255))
        screen.blit(text_surface, (10, 50 + 30 * i))

def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, 'RGBA', 1)
    width, height = texture_surface.get_size()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)

    return texture

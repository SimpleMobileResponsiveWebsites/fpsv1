import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
from gear import *
from inventory import Inventory
from pickup import HealthPickup, AmmoPickup
from ai import AI
from player import draw_player, handle_keys
from environment import Tree, Rock, Lake
from utils import display_inventory, load_texture

# Initialize Pygame
pygame.init()
pygame.font.init()

# Initialize GLUT
glutInit(sys.argv)

# Set up the display
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption('FPS Game')

# Player properties
player_pos = [0, 0, -5]
player_speed = 0.1
player_health = [100]  # Using a list to pass by reference

# Map size
MAP_SIZE = 1000

def generate_random_position(map_size):
    return [
        random.uniform(-map_size / 2, map_size / 2),
        0,
        random.uniform(-map_size / 2, map_size / 2)
    ]

def draw_terrain():
    glBegin(GL_LINES)
    for x in range(-MAP_SIZE // 2, MAP_SIZE // 2 + 1, 10):
        for z in range(-MAP_SIZE // 2, MAP_SIZE // 2 + 1, 10):
            glVertex3f(x, 0, -MAP_SIZE // 2)
            glVertex3f(x, 0, MAP_SIZE // 2)
            glVertex3f(-MAP_SIZE // 2, 0, z)
            glVertex3f(MAP_SIZE // 2, 0, z)
    glEnd()

def main():
    gluPerspective(45, (800 / 600), 0.1, 1000.0)
    glTranslatef(0.0, 0.0, -5)

    ai_opponents = [AI(*generate_random_position(MAP_SIZE)) for _ in range(5)]
    pickups = [
        HealthPickup(*generate_random_position(MAP_SIZE)),
        AmmoPickup(*generate_random_position(MAP_SIZE), 'pistol'),
        AmmoPickup(*generate_random_position(MAP_SIZE), 'rifle'),
        AmmoPickup(*generate_random_position(MAP_SIZE), 'shotgun'),
        Helmet(*generate_random_position(MAP_SIZE)),
        Headphones(*generate_random_position(MAP_SIZE)),
        ChestArmor(*generate_random_position(MAP_SIZE)),
        TacticalRig(*generate_random_position(MAP_SIZE)),
        Gun(*generate_random_position(MAP_SIZE)),
        Knife(*generate_random_position(MAP_SIZE)),
        FaceMask(*generate_random_position(MAP_SIZE)),
        Backpack(*generate_random_position(MAP_SIZE))
    ]
    environment_objects = [
        Tree(*generate_random_position(MAP_SIZE)),
        Tree(*generate_random_position(MAP_SIZE)),
        Rock(*generate_random_position(MAP_SIZE)),
        Rock(*generate_random_position(MAP_SIZE)),
        Lake(*generate_random_position(MAP_SIZE)),
        Lake(*generate_random_position(MAP_SIZE)),
    ]
    inventory = Inventory()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_keys(player_pos, player_speed)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the terrain
        draw_terrain()

        # Update and draw AI opponents
        for ai in ai_opponents:
            ai.update(player_pos, player_health)
            ai.draw()

        # Check and draw pickups
        for pickup in pickups[:]:
            if pickup.check_collision(player_pos):
                if isinstance(pickup, HealthPickup):
                    pickup.apply_effect(player_health)
                elif isinstance(pickup, AmmoPickup):
                    pickup.apply_effect(inventory)
                else:
                    inventory.add_gear(pickup)
                    print(f"Picked up {pickup.name}")
                pickups.remove(pickup)
            else:
                pickup.draw()

        # Draw environment objects
        for obj in environment_objects:
            obj.draw()

        draw_player(player_pos)

        # Display inventory
        display_inventory(screen, inventory)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

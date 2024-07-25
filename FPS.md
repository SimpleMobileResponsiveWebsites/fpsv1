FPS Game Project
Overview

This project is a simple first-person shooter (FPS) game implemented using Python with the Pygame and PyOpenGL libraries. The game features a player navigating through a 3D environment, interacting with various objects, AI opponents, and pickups. The player can move around, collect gear, and manage inventory.
Features

    3D Environment: Simple terrain with trees, rocks, and lakes.
    Player Movement: Control the player with WASD keys.
    AI Opponents: Basic AI entities that follow and attack the player.
    Pickups: Health and ammo pickups, as well as various gear items.
    Inventory System: Manage collected gear and ammo.
    Simple Graphics: Rendered using OpenGL for 3D objects and Pygame for 2D elements.

Requirements

    Python 3.8 or higher
    Pygame
    PyOpenGL

Installation

    Clone the repository:

    sh

git clone https://github.com/yourusername/fps-game.git
cd fps-game

Create a virtual environment:

sh

python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Install dependencies:

sh

    pip install -r requirements.txt

    Ensure texture file is present:
    Make sure you have the path_to_texture_image.png file in the project directory.

Running the Game

    Activate the virtual environment:

    sh

source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

Run the main script:

sh

    python main.py

Code Structure
main.py

The entry point of the game. Initializes Pygame and GLUT, sets up the display, and handles the main game loop.
player.py

Handles player movement and rendering.
gear.py

Defines various gear items that the player can collect.
inventory.py

Manages the player's inventory, including gear and ammo.
pickup.py

Defines health and ammo pickups, including their effects and rendering.
ai.py

Defines basic AI opponent behavior, including movement towards the player and attacking.
environment.py

Defines environmental objects like trees, rocks, and lakes.
utils.py

Contains utility functions for displaying the inventory and loading textures.
Usage

    Movement: Use WASD keys to move the player around.
    Collecting Items: Move close to an item to automatically collect it.
    Viewing Inventory: The inventory is displayed on the screen, showing collected gear and ammo count.

Future Improvements

    Enhanced Graphics: Improve the quality of models and textures.
    AI Behavior: Add more complex AI behaviors and different types of enemies.
    Combat System: Implement a more sophisticated combat system.
    UI Improvements: Enhance the inventory UI and add more interactive elements.

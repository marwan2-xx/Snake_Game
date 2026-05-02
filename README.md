🐍 Snake Game
A classic Snake game built with Python and Pygame, featuring clean object-oriented design.

🎮 Gameplay
Use the arrow keys to guide the snake around the grid. Eat the red food to grow longer and increase your score. The game ends if the snake hits a wall or runs into itself.

🏗️ Architecture
The project is structured around three core classes:
snake — Manages the snake's body (as a list of grid positions), movement logic, directional input, growth flag, and self-collision detection. Prevents 180° reversals by blocking opposite-direction inputs.
Food — Holds the food's current position and handles respawning to a random cell that doesn't overlap the snake's body.
Game — The main controller. Handles the game loop, collision detection (wall, self, and food), score tracking, Pygame rendering, and keyboard input.

🖥️ Rendering

Yellow square = snake head
Green squares = snake body
Red square = food
Score displayed in the top-left corner
Grid cells have small gaps for a clean visual separation

▶️ How to Run
pip install pygame
python game.py


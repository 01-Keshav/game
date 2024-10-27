Inspired by the classic Chrome browser dinosaur game, this project involves a dinosaur character that jumps over obstacles to accumulate points.

![Screenshot](utilities.webp

Features
Endless Runner: The dinosaur runs continuously, and the goal is to avoid obstacles as long as possible.
Score Tracking: Tracks the player's score based on how long they survive.
Difficulty Scaling: (Option to add) Increase game speed or frequency of obstacles as the score increases.
Game Over Screen: Displays a message and prompts the player to restart after collision with an obstacle.
Gameplay
Press SPACE to make the dinosaur jump.
Avoid colliding with obstacles to keep running and increase your score.
Press ESC to exit the game.
Requirements
Python 3.x
Pygame library
Install Pygame using pip:

pip install pygame
How to Run
Clone or download the repository.
Navigate to the project directory.
Run the game using Python:
python dinosaur_game.py
Code Structure
Dinosaur Class: Handles the dinosaur character's position, jump mechanism, and collision with the ground.
Obstacle Class: Creates obstacles that move toward the dinosaur, and handles off-screen removal.
Game Class: Manages game state, score, events, obstacle spawning, and collision detection.
Future Enhancements
Sound Effects: Add sounds for jumping and game over events.
Difficulty Scaling: Increase game speed as the score increases.
Animated Dinosaur: Use sprite images to add a running animation.
Parallax Background: Create a scrolling background for a more immersive experience.

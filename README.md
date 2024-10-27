<<<<<<< HEAD
# Dindinosaur game
Inspired by the classic Chrome browser dinosaur game, this project involves a dinosaur character that jumps over obstacles to accumulate points.
=======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dinosaur Game Documentation</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css">
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="container mx-auto px-4 py-8 max-w-4xl">
        <header class="text-center mb-12">
            <h1 class="text-4xl font-bold text-gray-800 mb-4">Dinosaur Game</h1>
            <p class="text-lg text-gray-600">A simple 2D endless runner game built with Python and Pygame</p>
        </header>
>>>>>>> 692dd20a481cf145e5392de5d2de9e2a244d855b

        <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
            <p class="text-gray-700 mb-4">
                Inspired by the classic Chrome browser dinosaur game, this project involves a dinosaur character that jumps over obstacles to accumulate points.
            </p>

<<<<<<< HEAD
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

1.Clone or download the repository.
2.Navigate to the project directory.
3.Run the game using Python:
4.python dinosaur_game.py

Code Structure

Dinosaur Class: Handles the dinosaur character's position, jump mechanism, and collision with the ground.

Obstacle Class: Creates obstacles that move toward the dinosaur, and handles off-screen removal.

Game Class: Manages game state, score, events, obstacle spawning, and collision detection.

Future Enhancements

Sound Effects: Add sounds for jumping and game over events.
Difficulty Scaling: Increase game speed as the score increases.
Animated Dinosaur: Use sprite images to add a running animation.
Parallax Background: Create a scrolling background for a more immersive experience.
=======
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Features</h2>
            <ul class="list-disc list-inside mb-6 text-gray-700">
                <li class="mb-2"><strong>Endless Runner:</strong> The dinosaur runs continuously, and the goal is to avoid obstacles as long as possible.</li>
                <li class="mb-2"><strong>Score Tracking:</strong> Tracks the player's score based on how long they survive.</li>
                <li class="mb-2"><strong>Difficulty Scaling:</strong> (Option to add) Increase game speed or frequency of obstacles as the score increases.</li>
                <li class="mb-2"><strong>Game Over Screen:</strong> Displays a message and prompts the player to restart after collision with an obstacle.</li>
            </ul>

            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Gameplay</h2>
            <ul class="list-disc list-inside mb-6 text-gray-700">
                <li class="mb-2">Press <code class="bg-gray-100 px-2 py-1 rounded">SPACE</code> to make the dinosaur jump.</li>
                <li class="mb-2">Avoid colliding with obstacles to keep running and increase your score.</li>
                <li class="mb-2">Press <code class="bg-gray-100 px-2 py-1 rounded">ESC</code> to exit the game.</li>
            </ul>
        </div>

        <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Requirements</h2>
            <ul class="list-disc list-inside mb-6 text-gray-700">
                <li class="mb-2">Python 3.x</li>
                <li class="mb-2">Pygame library</li>
            </ul>

            <div class="bg-gray-100 p-4 rounded-lg mb-6">
                <p class="text-gray-700 mb-2">Install Pygame using pip:</p>
                <code class="block bg-gray-800 text-white p-3 rounded">pip install pygame</code>
            </div>

            <h2 class="text-2xl font-semibold text-gray-800 mb-4">How to Run</h2>
            <ol class="list-decimal list-inside mb-6 text-gray-700">
                <li class="mb-2">Clone or download the repository.</li>
                <li class="mb-2">Navigate to the project directory.</li>
                <li class="mb-2">Run the game using Python:</li>
            </ol>
            <div class="bg-gray-800 text-white p-3 rounded mb-6">
                <code>python dinosaur_game.py</code>
            </div>
        </div>

        <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Code Structure</h2>
            <ul class="list-disc list-inside mb-6 text-gray-700">
                <li class="mb-2"><strong>Dinosaur Class:</strong> Handles the dinosaur character's position, jump mechanism, and collision with the ground.</li>
                <li class="mb-2"><strong>Obstacle Class:</strong> Creates obstacles that move toward the dinosaur, and handles off-screen removal.</li>
                <li class="mb-2"><strong>Game Class:</strong> Manages game state, score, events, obstacle spawning, and collision detection.</li>
            </ul>

            <h2 class="text-2xl font-semibold text-gray-800 mb-4">Future Enhancements</h2>
            <ol class="list-decimal list-inside mb-6 text-gray-700">
                <li class="mb-2"><strong>Sound Effects:</strong> Add sounds for jumping and game over events.</li>
                <li class="mb-2"><strong>Difficulty Scaling:</strong> Increase game speed as the score increases.</li>
                <li class="mb-2"><strong>Animated Dinosaur:</strong> Use sprite images to add a running animation.</li>
                <li class="mb-2"><strong>Parallax Background:</strong> Create a scrolling background for a more immersive experience.</li>
            </ol>
        </div>

        <footer class="text-center text-gray-600 mt-12">
            <p>This project is licensed under the MIT License.</p>
        </footer>
    </div>
</body>
</html>
>>>>>>> 692dd20a481cf145e5392de5d2de9e2a244d855b

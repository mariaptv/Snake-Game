
# Snake Game

This is a classic Snake game built using Python's `turtle` graphics library. The game allows users to control a snake on the screen, eat food, and grow in size. The objective is to avoid hitting the walls or the snake's own tail.

## Features

- Move the snake using the arrow keys (Up, Down, Left, Right).
- The snake grows each time it eats food.
- The score increases each time the snake eats food.
- The game ends if the snake collides with the walls or its own tail.
- A scoreboard to track the player's score.

## Requirements

- Python 3.x
- `turtle` library (comes pre-installed with Python)
- `time` and `random` modules (both are part of the Python Standard Library)

## How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/snake-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd snake-game
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## Controls

- **Up Arrow**: Move the snake up
- **Down Arrow**: Move the snake down
- **Right Arrow**: Move the snake right
- **Left Arrow**: Move the snake left

## Game Components

- **Snake**: The snake starts with three segments and grows each time it eats food. The snake can be controlled using the arrow keys.
- **Food**: A small circle that appears randomly on the screen. When the snake eats it, the food is repositioned.
- **Scoreboard**: Tracks the current score. The score increases each time the snake eats food. If the snake hits a wall or its own tail, the game ends, and "Game Over" is displayed.

## Code Structure

- `snake.py`: Contains the `Snake` class, which defines the snake's movement and growth mechanics.
- `food.py`: Contains the `Food` class, responsible for generating food at random positions on the screen.
- `scoreboard.py`: Contains the `Scoreboard` class, which handles displaying and updating the player's score.
- `main.py`: The main game loop where all components are initialized and the game logic runs.

## Screenshots

![image](https://github.com/user-attachments/assets/c62a665c-bd04-42ed-b6c8-27f3010291d9)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker Version](https://img.shields.io/badge/docker-20.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/paujorques02/hangman)

# Hangman Game

A Python-based implementation of the classic Hangman game. The game allows users to either play against the computer or observe the computer solving words automatically. This project is containerized using Docker to ensure consistency across development and production environments.

## Table of Contents
- [Hangman Game](#hangman-game)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Interactive Mode](#interactive-mode)
  - [Game Modes](#game-modes)
  - [Project Structure](#project-structure)
  - [Configuration](#configuration)
    - [Docker Compose Settings](#docker-compose-settings)
  - [Example Output](#example-output)
    - [Game Start](#game-start)
    - [Gameplay](#gameplay)
    - [End of the game](#end-of-the-game)
    - [Example Content of `results` file](#example-content-of-results-file)

## Overview

The Hangman Game project is designed for simplicity and ease of deployment. The game offers two modes:
- **Player vs. Machine**: The player attempts to guess the word generated by the computer.
- **Machine vs. Machine**: The computer plays autonomously, attempting to guess a set of words.

This project leverages Docker for a fully containerized environment, making it easy to set up and run the game across different platforms.

## Requirements

- [Docker](https://www.docker.com/get-started) (version 20.10 or higher)
- [Docker Compose](https://docs.docker.com/compose/) (version 1.29 or higher)

## Installation

1. **Clone the Repository**:
   Clone the repository to your local machine.
   ```bash
   git clone https://github.com/paujorques02/hangman.git
   cd hangman
   ```

2. **Directory Structure**:
    ```bash
    hangman/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── files.py
    ├── functions.py
    ├── hangman.py
    ├── play_machine.py
    ├── play_player.py
    ├── requirements.txt
    ├── results/            # Directory for storing game results
    ├── words/              # Directory containing word lists
    └── README.md
    ```

3. **Build and Start the Application**:
    ```bash
    docker compose up --build
    ```
    This will create a Docker container, install dependecies, and start the game.

## Usage 

### Interactive Mode

1. **Start the game**:
    ```bash
    docker-compose run --rm hangman
    ```

2. **Follow In-Game Prompts**:
    Follow the instructions on-screen to start playing.

3. **Stop the aplication**:
    To stop the game you can stop with any of the exits offered by the in-game prompts. Alternatively, you can shut down all running containers with:
    ```bash
    docker-compose down
    ```

## Game Modes

1. **Play Against the Machine**: Manually guess the letters in the word within a set number of attempts. Select your difficulty level to adjust the number of allowed guesses.
2. **Machine Plays Automatically**: Watch the computer attempt to guess a series of words on its own.

## Project Structure

* `Dockerfile`: Specifies the base image and dependencies required to run the Hangman game in a containerized environment.

* `docker-compose.yml`: Manages multi-container applications and specifies volume mappings for persistent storage of results and word files.

* `hangman.py`: The main entry point of the application. Handles initial user interaction and mode selection.

* `files.py`, `functions.py`, `play_machine.py`, `play_player.py`: Supporting modules that define the game logic, helper functions, and input/output handling. Each module is focused on a specific aspect of the game, ensuring a clean and modular codebase.

    * `files.py`: Handles file operations, such as reading word lists and saving game results.
    * `functions.py`: Contains utility functions, including word selection and difficulty settings.
    * `play_machine.py` and `play_player.py`: Define game modes, enabling interaction with the player or automatic gameplay by the machine.

* `results/`: Stores game outcome files generated by the application.

* `words/`: Contains any word lists required for gameplay.

## Configuration

### Docker Compose Settings

* **Volumes**: The `results` and `words` directories are mapped as volumes, ensuring that data persists even when the container is restarted or removed.

  * `results/`: Stores results for review or analysis.
  * `words/`: Holds text files with word lists for gameplay.

## Example Output

Below is a sample output of the game when running in **Player vs. Machine** mode with a difficulty level set to "Normal" (16 attempts).

### Game Start
```plaintext
Select one option to play the hangman game:

    1) Play against the machine.
    2) Machine plays automatically.
    X) Exit.

Introduce your option: 1

Choose a difficulty:
    1) Easy game: 20 attempts
    2) Normal game: 16 attempts
    3) Hard game: 12 attempts
    4) Impossible game: 10 attempts

Introduce your option: 2

How many words do you want to play? 1
```
### Gameplay
```plaintext
This is the word number 1 to be guessed.

You have 16 attempts to guess the word.

Your current word is: _ _ _ _ _ _

Introduce a letter: e

The character 'e' appears 1 time in the word.

You have 15 attempts left.
Current word is: _ e _ _ _ _

Introduce a letter: a

The character 'a' appears 2 times in the word.

You have 14 attempts left.
Current word is: _ e _ a _ a

Introduce a letter: t

The letter 't' is not in the word.

You have 13 attempts left.
Current word is: _ e _ a _ a

...
```
### End of the game
```plaintext
Congratulations! You have guessed the word "zebra".

Game Over.
```
In this example:

  * The player was able to guess the word "zebra" by selecting letters one at a time.
  * The game provides feedback on each guess, showing the updated word and the number of attempts remaining.
  
### Example Content of `results` file

After finishing the game, the application generates a results file in the results/ directory. Here’s an example of what the file might look like if the game is completed:

```plaintext
The word to guess was ZEBRA. You solved it in 12 attempts.

Out of 1 words, you solved 1 and failed in 0. You used 12 attempts.
In this example:
```
The results file records the word to guess, the number of attempts taken, and whether the word was solved.
It also summarizes the total number of words played, how many were correctly solved, how many were missed, and the total number of attempts used.


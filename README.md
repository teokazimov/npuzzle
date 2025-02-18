# N-Puzzle Solver using A* Search

## Overview
This project implements a solver for the N-puzzle (with grid sizes ranging from 3x3 to 6x6) using the A* search algorithm. The goal is to rearrange the sliding puzzle’s numbered tiles into sequential order with the fewest moves possible. The blank tile is represented as `0` (or an empty space in the input).

## Project Structure
- **helper.py**:  
  Provides utility functions for reading the puzzle configuration from a file and validating the grid dimensions.

- **heuristics.py**:  
  Implements two heuristic functions:
  - **Manhattan Distance**: Calculates the sum of the vertical and horizontal distances of each tile from its target position.
  - **Euclidean Distance**: Computes the straight-line distance between a tile’s current position and its goal position.

- **solver.py**:  
  Contains the A* search algorithm implementation. This module manages state expansion, cost calculation, and path reconstruction once the goal state is reached.

- **main.py**:  
  Serves as the entry point for the application. It reads the puzzle input, generates the goal state, and coordinates with the solver to find the solution.

- **input.txt**:  
  A sample input file that provides an initial puzzle configuration. Each line corresponds to a row in the puzzle, with numbers separated by whitespace (tabs or spaces). The blank tile is denoted by `0` or an empty space.

## Requirements
- Python 3.6 or above.
- No external libraries are needed; the project uses only standard Python modules.

## Setup and Execution

1. **Clone or Download the Repository**  
   Ensure that all Python files (`helper.py`, `heuristics.py`, `solver.py`, and `main.py`) and the `input.txt` file are in the same directory.

2. **Run the Solver**  
   Open your terminal (or command prompt) and navigate to the project directory. Execute the main script by running:
   ```bash
   python main.py input.txt
   ```
   If you are using a different input file, replace `input.txt` with the appropriate file path.

## Input File Format
The input file should represent the puzzle in an n×n grid, where each row is on a new line and numbers are separated by tabs or spaces. For example:
```
  1   2   3   5  10 
  6   7   4      15 
 11  12   9   8  20 
 16  17  13  14  23 
 21  22  18  24  19 
```
- The grid must have a size between 3x3 and 6x6.
- Ensure each row contains the correct number of elements. The program includes error handling to check for invalid configurations.

## How the Code Works
- **Puzzle Loading**:  
  The `load_puzzle` function in `helper.py` reads the puzzle from the specified file, ensuring the grid is valid and correctly formatted.

- **Goal State Generation**:  
  The `create_goal` function (found in multiple modules) generates the target configuration based on the size of the puzzle.

- **Heuristics**:  
  The Manhattan distance (default) is used to guide the A* search algorithm efficiently. The Euclidean distance function is also provided for experimentation.

- **A* Search Algorithm**:  
  Implemented in `solver.py`, the A* algorithm:
  - Initializes a priority queue with the starting state.
  - Expands states by moving the blank tile in possible directions.
  - Uses the heuristic to evaluate each state's cost.
  - Reconstructs and outputs the optimal path when the goal state is reached.

## Modifying the Puzzle
- To change the puzzle configuration, modify the `input.txt` file or create a new text file with your desired configuration. The puzzle must adhere to the n×n format (3 ≤ n ≤ 6).

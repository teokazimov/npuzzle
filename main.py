from solver import PuzzleSolver
from helper import load_puzzle
import sys

def execute():
    """
    Executes the puzzle solver with the following steps:
      1. Loads the puzzle setup from 'input.txt'.
      2. Retrieves heuristic selection from command-line arguments:
         - 'm' for Manhattan (default)
         - 'e' for Euclidean
      3. Initializes the solver with the loaded puzzle.
      4. Attempts to find a solution.
      5. Displays the number of moves required or an error message if unsolvable.
    """
    config_file = 'input.txt'
    
    try:
        start_state = load_puzzle(config_file)
    except Exception as err:
        print(f"Failed to load puzzle: {err}")
        return
    
    try:
        method = sys.argv[1]
        if method not in "me":
            print("Invalid heuristic method")
            print("Options:")
            print(" e - Euclidean\n m (default) - Manhattan")
            return
    except IndexError:
        method = "m"

    try:
        solver = PuzzleSolver(start_state, heuristic=method)
    except ValueError as err:
        print(f"Puzzle setup error: {err}")
        return

    moves = solver.find_solution()
    if moves != -1:
        print("Solved in", moves, "steps")
    else:
        print("No possible solution.")
        
if __name__ == "__main__":
    execute()

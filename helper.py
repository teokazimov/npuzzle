from typing import List, Tuple

def load_puzzle(file_path: str) -> List[List[int]]:
    """
    Reads an n x n sliding puzzle from a file and returns it as a 2D list.
    """
    puzzle_data: List[List[int]] = []
    with open(file_path) as file:
        for line in file:
            tokens = line.rstrip("\n").split()
            row = [int(token) if token.isdigit() else 0 for token in tokens]
            puzzle_data.append(row)
    
    size = len(puzzle_data)
    if not (3 <= size <= 6):
        raise ValueError(f"Invalid puzzle size: {size}x{size}. Must be between 3 and 6.")
    
    for idx, row in enumerate(puzzle_data):
        while len(row) < size:
            row.insert(0, 0)
        if len(row) != size:
            raise ValueError(f"Row {idx+1} has {len(row)} elements; expected {size}.")
    
    return puzzle_data

def create_goal(size: int) -> Tuple[Tuple[int, ...], ...]:
    """
    Generates the goal configuration for an n x n puzzle.
    """
    goal_state = [[(i * size + j + 1) % (size * size) for j in range(size)] for i in range(size)]
    return tuple(tuple(row) for row in goal_state)

def locate_blank(state: List[List[int]], size: int) -> Tuple[int, int]:
    """
    Finds the (row, column) position of the blank tile (0) in the puzzle.
    """
    for x in range(size):
        for y in range(size):
            if state[x][y] == 0:
                return x, y
    return -1, -1

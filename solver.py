from queue import PriorityQueue
from heuristics import *
from helper import create_goal, locate_blank

class PuzzleSolver:
    """
    Handles the n x n sliding puzzle and implements A* search for solving.
    """
    
    def __init__(self, start_config, heuristic="m"):
        self.size = len(start_config)
        for idx, row in enumerate(start_config):
            if len(row) != self.size:
                raise ValueError(
                    f"Invalid row {idx+1}: expected {self.size} elements."
                )
        self.start_config = tuple(tuple(row) for row in start_config)
        
        if heuristic == "e":
            print("Using Euclidean Heuristic")
            self.heuristic = euclidean
        elif heuristic == "m":
            print("Using Manhattan Heuristic")
            self.heuristic = manhattan
        else:
            print("Unknown heuristic, defaulting to Manhattan")
            self.heuristic = manhattan
        
        self.goal_config = create_goal(self.size)
        
    def find_neighbors(self, state):
        blank_x, blank_y = locate_blank(state, self.size)
        neighbors = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in moves:
            new_x, new_y = blank_x + dx, blank_y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                new_state = [list(row) for row in state]
                new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
                neighbors.append(tuple(tuple(row) for row in new_state))
        return neighbors
    
    def find_solution(self):
        queue = PriorityQueue()
        init_h = self.heuristic(self.size, self.start_config)
        queue.put((init_h, 0, self.start_config))
        visited = set()
        
        while not queue.empty():
            _, steps, curr_state = queue.get()
            if curr_state == self.goal_config:
                return steps
            if curr_state in visited:
                continue
            visited.add(curr_state)
            for neighbor in self.find_neighbors(curr_state):
                if neighbor not in visited:
                    new_steps = steps + 1
                    h = self.heuristic(self.size, neighbor)
                    queue.put((new_steps + h, new_steps, neighbor))
        return -1
from pathfinding import calculate_path
from random import choice

DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]

class DecisionNode:
    def __init__(self, pos, iteration, direction=None):
        self.pos = pos
        self.iteration = iteration
        self.direction = direction
        self.children = []

class Person:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.history = DecisionNode(start_pos, 0)
        self.current_node = self.history
        self.disabled_dirs = []
        self.delay = False

    def take_turn(self, grid, exits, iteration):
    if self.delay:
        print(f"Persona en {self.pos} pierde turno.")
        self.delay = False
        return

    path = None
    for salida in exits:
        temp_path = calculate_path(grid, self.pos, salida, self.disabled_dirs)
        if temp_path and (not path or len(temp_path) < len(path)):
            path = temp_path

    if not path or len(path) < 2:
        print(f"ay muchachos... (sin salida desde {self.pos})")
        return

    next_pos = path[1]
    direction = (next_pos[0] - self.pos[0], next_pos[1] - self.pos[1])
    self.current_node = self._add_decision(next_pos, iteration, direction)
    self.pos = next_pos

    cell = grid[self.pos[0]][self.pos[1]]
    if cell == "T":
        from random import choice
        self.disabled_dirs.append(choice([(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]))
    elif cell == "R":
        self.delay = True

    def _add_decision(self, pos, iteration, direction):
        node = DecisionNode(pos, iteration, direction)
        self.current_node.children.append(node)
        return node

def print_decision_tree(node, prefix=""):
    print(
        f"{prefix}Iteración {node.iteration}: Celda {node.pos} {f'(→ {node.direction})' if node.direction else '(Inicio)'}")
    for child in node.children:
        print_decision_tree(child, prefix + "│   ")

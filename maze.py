"""For all code involving the maze generation"""
import random
import commons

# === MAZE GENERATION (DFS) WITH ENTRANCE ===
def generate_maze(size):
    global maze
    maze = [[1 for _ in range(size)] for _ in range(size)]
    stack = []

    entrance = (1, 0)
    maze[entrance[0]][entrance[1]] = 0
    maze[1][1] = 0

    stack.append((1, 1))
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    path = [(1,1)]

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[nx][ny] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(x + nx) // 2][(y + ny) // 2] = 0
            if random.random() < 0.8:
                maze[nx][ny] = 0
            stack.append((nx, ny))
            path.append((nx, ny))
        else:
            stack.pop()

    return maze, entrance

# === FIND RANDOM EMPTY CELL ===
def get_random_empty_cell(maze):
    while True:
        r = random.randint(0, commons.GRID_SIZE - 1)
        c = random.randint(0, commons.GRID_SIZE - 1)
        if maze[r][c] == 0:
            return (r, c)
        
def get_random_empty_min_cell(maze):
    while True:
        r = random.randint((commons.GRID_SIZE//2), commons.GRID_SIZE - 1)
        c = random.randint((commons.GRID_SIZE//2), commons.GRID_SIZE - 1)
        if maze[r][c] == 0:
            return (r, c)


# === SETUP MAZE ===
def setup():
    global _maze, entrance, inventory, inventory_items, available_items, items, item, hero_pos, minotaur_pos, minotaur_path, minotaur_timer, move_timer, MOVE_INTERVAL, held_keys, visitedfog, hero_hp, minotaur_hp
    hero_hp = 1000
    minotaur_hp = 2000

    
    _maze, entrance = generate_maze(commons.GRID_SIZE)
    hero_pos = entrance
    minotaur_pos = get_random_empty_min_cell(_maze)
    while minotaur_pos == hero_pos:
        minotaur_pos = get_random_empty_min_cell(_maze)


    #ADDED for the fog/visibility
    visitedfog = set()
    visitedfog.add(hero_pos)

    items = set()
    while len(items) < commons.NUM_ITEMS:
        item = get_random_empty_cell(_maze)
        if item != hero_pos and item != minotaur_pos:
            items.add(item)

    inventory = 0
    inventory_items = []

    minotaur_path = []
    minotaur_timer = 0
    move_timer = 0
    MOVE_INTERVAL = 0.1  # seconds between hero movement when key is held
    held_keys = {"up": False, "down": False, "left": False, "right": False}

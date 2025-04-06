import pygame
import random
import heapq

# === CONFIG ===
GRID_SIZE = 51  # Must be odd to ensure single-width walls
CELL_SIZE = 12
HUD_HEIGHT = 30
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE + HUD_HEIGHT)
FPS = 60
MINOTAUR_MOVE_INTERVAL = 0.8  # seconds between minotaur steps
NUM_ITEMS = 20  # Number of yellow squares

# === COLORS ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# === INIT PYGAME ===
pygame.init()
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Minotaur Chase")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# === MAZE GENERATION (DFS) WITH ENTRANCE ===
def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]
    stack = []

    entrance = (1, 0)
    maze[entrance[0]][entrance[1]] = 0
    maze[1][1] = 0

    stack.append((1, 1))
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

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
            maze[nx][ny] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze, entrance

# === A* ALGORITHM ===
def a_star(maze, start, goal):
    def h(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(h(start, goal), 0, start)]
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        visited.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and maze[nx][ny] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + h(neighbor, goal), tentative_g, neighbor))

    return []  # no path

# === FIND RANDOM EMPTY CELL ===
def get_random_empty_cell(maze):
    while True:
        r = random.randint(0, GRID_SIZE - 1)
        c = random.randint(0, GRID_SIZE - 1)
        if maze[r][c] == 0:
            return (r, c)

# === SETUP ===
maze, entrance = generate_maze(GRID_SIZE)
hero_pos = entrance
minotaur_pos = get_random_empty_cell(maze)
while minotaur_pos == hero_pos:
    minotaur_pos = get_random_empty_cell(maze)

items = set()
while len(items) < NUM_ITEMS:
    item = get_random_empty_cell(maze)
    if item != hero_pos and item != minotaur_pos:
        items.add(item)

inventory = 0

minotaur_path = []
minotaur_timer = 0
move_timer = 0
MOVE_INTERVAL = 0.1  # seconds between hero movement when key is held
held_keys = {"up": False, "down": False, "left": False, "right": False}

# === GAME LOOP ===
running = True
while running:
    dt = clock.tick(FPS) / 1000
    move_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: held_keys["up"] = True
            elif event.key == pygame.K_DOWN: held_keys["down"] = True
            elif event.key == pygame.K_LEFT: held_keys["left"] = True
            elif event.key == pygame.K_RIGHT: held_keys["right"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: held_keys["up"] = False
            elif event.key == pygame.K_DOWN: held_keys["down"] = False
            elif event.key == pygame.K_LEFT: held_keys["left"] = False
            elif event.key == pygame.K_RIGHT: held_keys["right"] = False

    if move_timer >= MOVE_INTERVAL:
        dx, dy = 0, 0
        if held_keys["up"]: dx = -1
        elif held_keys["down"]: dx = 1
        elif held_keys["left"]: dy = -1
        elif held_keys["right"]: dy = 1

        new_pos = (hero_pos[0] + dx, hero_pos[1] + dy)
        if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE and maze[new_pos[0]][new_pos[1]] == 0:
            hero_pos = new_pos
            if hero_pos in items:
                items.remove(hero_pos)
                inventory += 1
        move_timer = 0

    # === MINOTAUR MOVEMENT ===
    minotaur_timer += dt
    if minotaur_timer >= MINOTAUR_MOVE_INTERVAL:
        minotaur_path = a_star(maze, minotaur_pos, hero_pos)
        if minotaur_path and len(minotaur_path) > 1:
            minotaur_pos = minotaur_path[1]
        minotaur_timer = 0

    # === DRAWING ===
    win.fill(WHITE)

    # Draw inventory bar
    pygame.draw.rect(win, WHITE, (0, 0, WINDOW_SIZE[0], HUD_HEIGHT))
    inventory_text = font.render(f"Inventory: {inventory}", True, (0, 0, 0))
    win.blit(inventory_text, (5, 5))

    # Draw maze offset below HUD
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            color = BLACK if maze[r][c] == 1 else WHITE
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE + HUD_HEIGHT, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(win, color, rect)

    for item in items:
        rect = pygame.Rect(item[1] * CELL_SIZE, item[0] * CELL_SIZE + HUD_HEIGHT, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(win, YELLOW, rect)

    pygame.draw.rect(win, BLUE, (hero_pos[1] * CELL_SIZE, hero_pos[0] * CELL_SIZE + HUD_HEIGHT, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(win, RED, (minotaur_pos[1] * CELL_SIZE, minotaur_pos[0] * CELL_SIZE + HUD_HEIGHT, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

pygame.quit()

import pygame
import heapq
import commons
import maze

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
            if 0 <= nx < commons.GRID_SIZE and 0 <= ny < commons.GRID_SIZE and maze._maze[nx][ny] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + h(neighbor, goal), tentative_g, neighbor))

    return []  # no path

def play(paused):
    
    if paused:
        return

    # === GAME LOOP ===

    running = True
    global pause_btn
    pause_btn = None #Initialization
    
    while running and not paused:
        
        dt = commons.clock.tick(commons.FPS) / 1000
        maze.move_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Program killed.")
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: maze.held_keys["up"] = True
                elif event.key == pygame.K_DOWN: maze.held_keys["down"] = True
                elif event.key == pygame.K_LEFT: maze.held_keys["left"] = True
                elif event.key == pygame.K_RIGHT: maze.held_keys["right"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: maze.held_keys["up"] = False
                elif event.key == pygame.K_DOWN: maze.held_keys["down"] = False
                elif event.key == pygame.K_LEFT: maze.held_keys["left"] = False
                elif event.key == pygame.K_RIGHT: maze.held_keys["right"] = False

        keys = pygame.key.get_pressed() #Gets state of all keys

        if maze.move_timer >= maze.MOVE_INTERVAL:
            dx, dy = 0, 0
            if keys[pygame.K_UP]: dx = -1
            elif keys[pygame.K_DOWN]: dx = 1
            elif keys[pygame.K_LEFT]: dy = -1
            elif keys[pygame.K_RIGHT]: dy = 1

            new_pos = (maze.hero_pos[0] + dx, maze.hero_pos[1] + dy)
            if 0 <= new_pos[0] < commons.GRID_SIZE and 0 <= new_pos[1] < commons.GRID_SIZE and maze._maze[new_pos[0]][new_pos[1]] == 0:
                maze.hero_pos = new_pos
                if maze.hero_pos in maze.items:
                    maze.items.remove(maze.hero_pos)
                    maze.inventory += 1
            maze.move_timer = 0

        # === MINOTAUR MOVEMENT ===
        maze.minotaur_timer += dt
        if maze.minotaur_timer >= commons.MINOTAUR_MOVE_INTERVAL:
            maze.minotaur_path = a_star(maze, maze.minotaur_pos, maze.hero_pos)
            if maze.minotaur_path and len(maze.minotaur_path) > 1:
                maze.minotaur_pos = maze.minotaur_path[1]
            maze.minotaur_timer = 0

        # === DRAWING ===
        commons.screen.fill(commons.white)
        
        pause_btn = commons.put_button('Pause', 'Arial Bold', 30, commons.black, 0, commons.bronze, commons.black, 5, commons.screen, 70, 20)

        # Draw inventory bar
        pygame.draw.rect(commons.screen, commons.white, (0, 0, commons.WINDOW_SIZE[0], commons.HUD_HEIGHT))
        commons.draw_text(f"Inventory:  {maze.inventory}", 'Arial Bold', 30, commons.black, commons.screen, 70, 20)

        # Draw maze offset below HUD
        for r in range(commons.GRID_SIZE):
            for c in range(commons.GRID_SIZE):
                color = commons.black if maze._maze[r][c] == 1 else commons.white
                rect = pygame.Rect(c * commons.CELL_SIZE, r * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE)
                pygame.draw.rect(commons.screen, color, rect)

        for maze.item in maze.items:
            rect = pygame.Rect(maze.item[1] * commons.CELL_SIZE, maze.item[0] * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE)
            pygame.draw.rect(commons.screen, commons.pale_yellow, rect)

        pygame.draw.rect(commons.screen, commons.bronze, (maze.hero_pos[1] * commons.CELL_SIZE, maze.hero_pos[0] * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE))
        pygame.draw.rect(commons.screen, commons.red_brown, (maze.minotaur_pos[1] * commons.CELL_SIZE, maze.minotaur_pos[0] * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE))

        pygame.display.flip()

    pygame.quit()
    return pause_btn
import pygame
import heapq
import random
import commons
import maze
import links
import death_screen
import hero

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

#minatour attacking function
def min_attack():
    if maze.hero_pos == maze.minotaur_pos and not shield:
        maze.hero_hp -= 10
def play(paused):
    
    if paused:
        return

    # === GAME LOOP ===

    running = True
    global pause_btn, item_message, item_timer, sword, shield
    pause_btn = None #Initialization
    
    while running and not paused:
        
        if not pygame.display.get_init():
            return
        
        dt = commons.clock.tick(commons.FPS) / 1000
        maze.move_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                commons.exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    commons.paused = True
                    return  #Go to main menu, Game paused
                elif event.key == pygame.K_i:
                    commons.inventory_open = not commons.inventory_open
                    return  #Go to inventory, Game paused
                elif event.key == pygame.K_UP: maze.held_keys["up"] = True
                elif event.key == pygame.K_DOWN: maze.held_keys["down"] = True
                elif event.key == pygame.K_LEFT: maze.held_keys["left"] = True
                elif event.key == pygame.K_RIGHT: maze.held_keys["right"] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: maze.held_keys["up"] = False
                elif event.key == pygame.K_DOWN: maze.held_keys["down"] = False
                elif event.key == pygame.K_LEFT: maze.held_keys["left"] = False
                elif event.key == pygame.K_RIGHT: maze.held_keys["right"] = False

        if commons.playing and commons.running:
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
                maze.visitedfog.add(maze.hero_pos)
                if maze.hero_pos in maze.items:
                    maze.items.remove(maze.hero_pos)
                    picked = random.choice(links.available_items)
                    links.available_items.remove(picked)
                    maze.inventory_items.append(picked)
                    maze.inventory += 1
                    item_message = f"Picked up: {picked['name']}"
                    item_timer = pygame.time.get_ticks() + 2000
                    
            maze.move_timer = 0
            item_message = None
            item_timer = 0

        
        # === MINOTAUR MOVEMENT ===
        maze.minotaur_timer += dt
        if maze.minotaur_timer >= commons.MINOTAUR_MOVE_INTERVAL:
            maze.minotaur_path = a_star(maze, maze.minotaur_pos, maze.hero_pos)
            if maze.minotaur_path and len(maze.minotaur_path) > 1:
                maze.minotaur_pos = maze.minotaur_path[1]
            maze.minotaur_timer = 0

        #checking items of hero
        sword, shield = hero.has_sword_or_shield(maze.inventory_items)

        # === HERO ATTACK ===
        hero.hero_attack()

        # === MINOTAUR ATTACK ===
        min_attack()

        #checking if hero is dead
        if maze.hero_hp <= 0:
            death_screen.death_screen()
            return
        #checking if minatour is dead
        if maze.minotaur_hp <= 0:
            death_screen.defeated_min()
            return
        

        # === DRAWING ===
        if not pygame.display.get_init():
            return
        commons.screen.fill(commons.white)
        
        # Draw inventory bar
        pygame.draw.rect(commons.screen, commons.white, (0, 0, commons.WINDOW_SIZE[0], commons.HUD_HEIGHT))
        commons.draw_text(f"Inventory:  {maze.inventory}", 'Arial Bold', 30, commons.black, commons.screen, 70, 20)

        #display hp stat
        commons.draw_text(f"Hero HP", 'Arial Bold', 30, commons.black, commons.screen, 250, 20)
        commons.draw_text(f"Minotaur HP", 'Arial Bold', 30, commons.black, commons.screen, 500, 20)
        #hero health bar
        commons.draw_health_bar(commons.screen, 300, 10, 100, 20, maze.hero_hp, 1000, (0,255,0))
        #minatour health bar
        commons.draw_health_bar(commons.screen, 570, 10, 100, 20, maze.minotaur_hp, 2000, (255,0,0))
        

        # Draw maze offset below HUD
        for r in range(commons.GRID_SIZE):
            for c in range(commons.GRID_SIZE):
                cell_pos = (r,c)
                visible = False

                if cell_pos in maze.visitedfog:
                    visible = True
                elif abs(maze.hero_pos[0] - r) + abs(maze.hero_pos[1] - c) <= 2:
                    visible = True
                
                rect = pygame.Rect(c * commons.CELL_SIZE, r * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE)
            
                if visible:
                
                    color = commons.black if maze.maze[r][c] == 1 else commons.white
                    pygame.draw.rect(commons.screen, color, rect)
                else:
                    pygame.draw.rect(commons.screen, (30, 30, 30), rect)

        for maze.item in maze.items:
            rect = pygame.Rect(maze.item[1] * commons.CELL_SIZE, maze.item[0] * commons.CELL_SIZE + commons.HUD_HEIGHT, commons.CELL_SIZE, commons.CELL_SIZE)
            commons.screen.blit(commons.artifact_img, rect)

        commons.screen.blit(commons.hero_img, (maze.hero_pos[1] * commons.CELL_SIZE, maze.hero_pos[0] * commons.CELL_SIZE + commons.HUD_HEIGHT))
        commons.screen.blit(commons.minotaur_img, (maze.minotaur_pos[1] * commons.CELL_SIZE, maze.minotaur_pos[0] * commons.CELL_SIZE + commons.HUD_HEIGHT))

        

        if not pygame.display.get_init():
            return
        pygame.display.flip()




    pygame.quit()

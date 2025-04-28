##death screen will move later after testing
import pygame
import commons
import gameplay
import maze
import links

def reset_stat():
    maze.items.clear()
    maze.inventory.clear()
    maze.inventory_items.clear()

def death_screen():
        font = pygame.font.SysFont('Arial', 50)
        small_font = pygame.font.SysFont('Arial', 30)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    commons.exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        commons.paused = True
                        commons.playing = False
                        commons.state = 'menu'
                        for item in maze.inventory_items[:]:  
                               maze.inventory_items.remove(item)
                               links.available_items.append(item)
                        gameplay.main()
                        return  #Go back to main menu

            commons.screen.fill((0, 0, 0))  # Black background
            text = font.render("You have died!", True, (255, 0, 0))
            info = small_font.render("Press ENTER to return to Main Menu", True, (255, 255, 255))
            commons.screen.blit(text, (commons.WINDOW_SIZE[0] // 2 - text.get_width() // 2, commons.WINDOW_SIZE[1] // 3))                
            commons.screen.blit(info, (commons.WINDOW_SIZE[0] // 2 - info.get_width() // 2, commons.WINDOW_SIZE[1] // 2))
            pygame.display.flip()

def defeated_min():
        
        font = pygame.font.SysFont('Arial', 50)
        small_font = pygame.font.SysFont('Arial', 30)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    commons.exit_game()  
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        commons.paused = False 
                        commons.state = 'playing'  
                        return  

                    elif event.key == pygame.K_ESCAPE:
                        commons.paused = True
                        commons.state = 'menu'
                        return
                
            commons.screen.fill((0, 0, 0))  # Black background
            text = font.render("You have defeated the minotaur!", True, (255, 0, 0))
            info = small_font.render("Press ENTER to return to the start", True, (255, 255, 255))
            commons.screen.blit(text, (commons.WINDOW_SIZE[0] // 2 - text.get_width() // 2, commons.WINDOW_SIZE[1] // 3))                
            commons.screen.blit(info, (commons.WINDOW_SIZE[0] // 2 - info.get_width() // 2, commons.WINDOW_SIZE[1] // 2))
            pygame.display.flip()
    

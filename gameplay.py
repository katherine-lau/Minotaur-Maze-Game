"""For all code involving the gameplay"""
import pygame
import maze
import minotaur
import commons

#Main menu screen
def main_menu(playing):
    if not pygame.display.get_init():
        return
    commons.screen.fill(commons.red_brown)
    commons.draw_text('MAIN MENU', 'Arial', 40, commons.black, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4)  #main menu title
    """CODE FOR MAIN MENU BUTTONS GO HERE"""
    menu = {}
    #if playing -> use "start game" button, else -> use "resume game" button
    if playing:
        menu['rs_button'] = commons.put_button('Resume Game', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 2)
    else:
        menu['rs_button'] = commons.put_button('Start Game', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 2)
    
    #manual button
    menu['manual_button'] = commons.put_button('Manual', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 5)
    
    #quit button
    menu['quit_button'] = commons.put_button('Quit', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4 * 3)
    
    pygame.display.flip()
    return menu

#Inventory screen
def inventory():
    if not pygame.display.get_init():
        return
    if commons.inventory_open:
        pygame.draw.rect(commons.screen, commons.bronze, (0, commons.WINDOW_SIZE[1] / 2, commons.WINDOW_SIZE[0], commons.WINDOW_SIZE[1]))
        commons.draw_text('INVENTORY', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 2 + 30)  #inventory title
        commons.draw_text(f'Items: {maze.inventory}', 'Arial', 20, commons.black, commons.screen, 40, commons.WINDOW_SIZE[1] / 20 * 11)
        
        pygame.draw.rect(commons.screen, commons.white, (0, commons.WINDOW_SIZE[1] * 9 / 16, commons.WINDOW_SIZE[0], commons.WINDOW_SIZE[1]))
        
        #item slots
        s_width = 80
        s_height = 80
        spacing = 20
        start_x = 20
        start_y = commons.WINDOW_SIZE[1] * 9 / 16 + 20
        
        ipr = (commons.WINDOW_SIZE[0] - start_x * 2) // (s_width + spacing)
        hovered = None
        
        for i, item in enumerate(maze.inventory_items):
            row = i // ipr
            col = i % ipr
            x = start_x + col * (s_width + spacing)
            y = start_y + row * (s_height + spacing)
            
            slot = pygame.Rect(x, y, s_width, s_height)
            pygame.draw.rect(commons.screen, commons.pale_yellow, slot)
            pygame.draw.rect(commons.screen, commons.black, slot, 2)
            
            icon = pygame.transform.scale(item["icon"], (50, 50))
            icon_pos = (x + (s_width - 50) //2, y + 5)
            commons.screen.blit(icon, icon_pos)
            
            commons.draw_text(item["name"], 'Arial', 12, commons.black, commons.screen, x + s_width / 2, y + s_height - 15)

            #Detect hover
            if slot.collidepoint(pygame.mouse.get_pos()):
                hovered = item
                
            if hovered:
                popup_txt = f"{hovered['description']}"
                font = pygame.font.SysFont('Arial', 16)
                text = font.render(popup_txt, True, commons.red_brown)
                rect = text.get_rect()
                rect.bottomleft = (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] + 10)
                pygame.draw.rect(commons.screen, commons.pale_yellow, rect.inflate(10, 10))
                pygame.draw.rect(commons.screen, commons.black, rect.inflate(10, 10), 2)
                commons.screen.blit(text, rect)


            #item picked up
            current_time = pygame.time.get_ticks()
            if minotaur.item_message and current_time < minotaur.item_timer:
                font = pygame.font.SysFont('Arial', 24)
                text = font.render(minotaur.item_message, True, commons.bronze)
                rect = text.get_rect(center = (commons.WINDOW_SIZE[0] // 2, commons.WINDOW_SIZE[1] // 2 - 100))
                
                pygame.draw.rect(commons. screen, commons. black, rect.inflate(20, 10))
                commons.screen.blit(text, rect)
            elif minotaur.item_message and current_time >= minotaur.item_timer:
                minotaur.item_message = None
        
        pygame.display.flip()
        
#Manual screen
def manual():
    if not pygame.display.get_init():
        return
    commons.screen.fill(commons.bronze)
    commons.draw_text('HOW TO PLAY', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4)
    commons.draw_text(' - Use arrow keys to move', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 3)
    commons.draw_text(' - I to open inventory (tap I again to close)', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 4)
    commons.draw_text(' - Double tap ESC to pause and then open main menu', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 5)
    commons.draw_text('Press ESC to return', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 6)
    pygame.display.flip()
    
"""Main()"""
def main(): #Where all the code is going to go
    global ctrl_pressed, menu
    commons.running = True  #Show program is running
    commons.playing = False #Show main menu upon startup
    commons.paused = True  #Show main menu first
    commons.inventory_open = False
    ctrl_pressed = False    #track if ctrl key is pressed for quit
    
    #resetting the speed of hero and minatour
    maze.MOVE_INTERVAL = 0.1
    commons.MINOTAUR_MOVE_INTERVAL = 0.5 
    
    commons.game_start()
    print("Game started.")
    maze.setup()
    
    while commons.running:
        if not pygame.display.get_init():
            break
        
        if commons.state == 'menu':
            menu = main_menu(commons.playing)
        elif commons.state == 'manual':
            manual()
        elif commons.state == 'playing' and commons.inventory_open:
            inventory()
        elif commons.state == 'playing':
            minotaur.play(commons.paused)
        
        
        
        if not pygame.display.get_init():
            break
        
        mouse = pygame.mouse.get_pos()
        quit_btn = menu.get('quit_button', None)
        manual_btn = menu.get('manual_button', None)
        rs_btn = menu.get('rs_button', None)
    
        #program quit, game start, game pause
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #close button clicked -> game quits and closes
                commons.exit_game()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:  #mouse click
                if quit_btn and quit_btn.collidepoint(mouse):
                    commons.exit_game()
                    break
                elif rs_btn and rs_btn.collidepoint(mouse):
                    commons.playing = True
                    commons.paused = False
                    commons.state = 'playing'
                if manual_btn and manual_btn.collidepoint(mouse):
                    commons.state = 'manual'
            elif event.type == pygame.KEYDOWN:  #key click
                if event.key == pygame.K_ESCAPE:
                    if commons.state == 'manual':
                        commons.state = 'menu'
                    elif commons.state == 'menu':
                        if commons.playing:
                            commons.paused = False
                            commons.state = 'playing'
                    elif commons.state == 'playing':
                        if commons.inventory_open:
                            commons.inventory_open = False
                            commons.paused = False
                        else:
                            commons.paused = True
                            commons.state = 'menu'
                elif event.key == pygame.K_i:
                    if commons.state == 'playing':
                        commons.inventory_open = not commons.inventory_open
                        commons.paused = commons.inventory_open
        if not pygame.display.get_init():
            return
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":  #so game is only run when wanted, __name__ = name of file
    main()

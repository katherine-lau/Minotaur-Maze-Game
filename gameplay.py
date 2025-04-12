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
        pygame.draw.rect(commons.screen, commons.white, (0, commons.WINDOW_SIZE[1] / 16 * 9, commons.WINDOW_SIZE[0], commons.WINDOW_SIZE[1]))
        commons.draw_text(f'Items: {maze.inventory}', 'Arial', 20, commons.black, commons.screen, 40, commons.WINDOW_SIZE[1] / 20 * 11)
        """OTHER CODE FOR INVENTORY ITEMS"""
        
        pygame.display.flip()
        
#Manual screen
def manual():
    if not pygame.display.get_init():
        return
    commons.screen.fill(commons.bronze)
    commons.draw_text('HOW TO PLAY', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4)
    commons.draw_text(' - Use arrow keys to move', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 3)
    commons.draw_text(' - I to open inventory (tap I again to close)', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 4)
    commons.draw_text(' - Double tap ESC to pause', 'Arial', 40, commons.pale_yellow, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 8 * 5)
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
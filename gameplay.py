"""For all code involving the gameplay"""
import pygame
import maze
import minotaur
import commons

#Main menu screen
def main_menu(playing):
    commons.screen.fill(commons.red_brown)
    commons.draw_text('MAIN MENU', 'Arial', 40, commons.black, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4)  #main menu title
    """CODE FOR MAIN MENU BUTTONS GO HERE"""
    menu = {}
    #if playing -> use "start game" button, else -> use "resume game" button
    if playing:
        menu['rs_button'] = commons.put_button('Resume Game', 'Arial', 40, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 2)
    else:
        menu['rs_button'] = commons.put_button('Start Game', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 2)
    
    #quit button
    menu['quit_button'] = commons.put_button('Quit', 'Arial', 20, commons.black, 20, commons.pale_yellow, commons.black, 10, commons.screen, commons.WINDOW_SIZE[0] / 2, commons.WINDOW_SIZE[1] / 4 * 3)
    
    pygame.display.flip()
    return menu


"""Main()"""
def main(): #Where all the code is going to go
    global ctrl_pressed, menu
    commons.running = True  #Show program is running
    commons.playing = False #Show main menu upon startup
    commons.paused = True  #Show main menu first
    ctrl_pressed = False    #track if ctrl key is pressed for quit
    
    commons.game_start()
    print("Game started.")
    maze.setup()
    
    while commons.running:
        global pause_btn
        if commons.paused:  #show main menu when paused
            menu = main_menu(commons.playing)
        
        pause_btn = minotaur.play(commons.paused)
        
        if pygame.display.get_init():
            mouse = pygame.mouse.get_pos()
            quit_btn = menu.get('quit_button', None)
            rs_btn = menu.get('rs_button', None)
        
            #program quit, game start, game pause
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #close button clicked -> game quits and closes
                    print("Program killed.")
                    commons.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN:  #mouse click
                    if quit_btn and quit_btn.collidepoint(mouse):
                        commons.running = False
                    elif rs_btn and rs_btn.collidepoint(mouse):
                        if commons.playing:
                            commons.paused = False
                        else:
                            commons.playing = True
                            commons.paused = False
                elif event.type == pygame.KEYDOWN:  #key click
                    if event.key == pygame.K_ESCAPE:
                        commons.paused = not commons.paused
                        print("Game paused.")
        if pygame.display.get_init():
            pygame.display.flip()
    pygame.quit()
    print("Game closed.")

if __name__ == "__main__":  #so game is only run when wanted, __name__ = name of file
    main()
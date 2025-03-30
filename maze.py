import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1080, 1080))  #window
pygame.display.set_caption("Minotaur Maze Game")

"""Colors"""
white = (255,255,255)
pale_yellow = (255,246,143)
bronze = (205,102,0)
red_brown = (139,37,0)
black = (0,0,0)

"""Fonts"""
font1 = pygame.font.SysFont(None, 200)
font2 = pygame.font.SysFont(None, 50)

#draw text on screen
def draw_text(text, font, fontcolor, surface, x, y):
    textobj = font.render(text, True, fontcolor)   #txt -> obj
    textrect = textobj.get_rect(center = (x,y))   #txt obj -> rectangle w/ txt centered
    surface.blit(textobj, textrect) #txt on surface
    
#put btn on screen
def put_button(text, font, fontcolor, padding, bgcolor, bordercolor, borderwidth, surface, x, y):
    textobj = font.render(text, True, fontcolor)   #txt -> obj
    textrect = textobj.get_rect()   #txt obj rectangle
    
    btnrect = pygame.Rect(0, 0, textrect.width + 2*padding, textrect.height + 2*padding)    #btn rectangle
    btnrect.center = (x,y) #center of txt @ (x,y)
    
    #draw border if there is one
    if bordercolor:
        pygame.draw.rect(surface, bordercolor, btnrect, borderwidth)
    
    #give btn a bg
    bg = btnrect.inflate(-borderwidth * 2, -borderwidth * 2)
    pygame.draw.rect(surface, bgcolor, bg)
    
    #put txt on bg
    textrect.center = btnrect.center
    surface.blit(textobj, textrect) #txt on btn
    
    return btnrect  #when button is clicked

#main menu screen
def main_menu(playing):
    screen.fill(red_brown)
    draw_text('MAIN MENU', font1, black, screen, 540, 200)  #main menu title
    """CODE FOR MAIN MENU BUTTONS GO HERE"""
    #if playing -> use "start game" button, else -> use "resume game" button
    if playing:
        sr_btn = put_button('Resume Game', font2, black, 20, pale_yellow, black, 10, screen, 540, 400)
    else:
        sr_btn = put_button('Start Game', font2, black, 20, pale_yellow, black, 10, screen, 540, 400)
    pygame.display.flip()
    return sr_btn

#ALL FUNCTIONS GO ABOVE main()
def main(): #Where all the code is going to go
    running = True
    playing = False #Show main menu upon startup
    paused = True  #Show main menu first
    while running:
        if paused:  #show main menu when paused
            sr_btn = main_menu(playing)
        
        #program quit, game start, game pause
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #close button clicked -> game quits and closes
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  #play button clicked
                mouse_pos = pygame.mouse.get_pos()
                if paused:  #menu open
                    if sr_btn.collidepoint(mouse_pos):
                        playing = True  #game started
                        paused = False  #game playing
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and playing:   #esc clicked -> toggle menu while paused
                    paused = not paused #pause/unpause game
                    
        if playing and not paused:
            """ALL GAME CODE GOES HERE"""
            screen.fill(white)  #this is dummy code
                    
        pygame.display.flip()
    
    
if __name__ == "__main__":  #so game is only run when wanted, __name__ = name of file
    main()

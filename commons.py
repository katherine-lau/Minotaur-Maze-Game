#for all common occurances to prevent import loops
import pygame

"""Screen vars"""
GRID_SIZE = 47  # Must be odd to ensure single-width walls
CELL_SIZE = 23
HUD_HEIGHT = 30
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE + HUD_HEIGHT)
FPS = 60
MINOTAUR_MOVE_INTERVAL = 0.8  # seconds between minotaur steps
NUM_ITEMS = 20  # Number of yellow squares

"""Color vars"""
white = (255,255,255)
pale_yellow = (255,246,143)
bronze = (205,102,0)
red_brown = (139,37,0)
black = (0,0,0)

#Sets font
def set_font(font, size):
    return pygame.font.SysFont(font, size)

#Draw text on screen
def draw_text(text, fonttype, fontsize, fontcolor, surface, x, y):
    font = set_font(fonttype, fontsize)
    textobj = font.render(text, True, fontcolor)   #txt -> obj
    textrect = textobj.get_rect(center = (x,y))   #txt obj -> rectangle w/ txt centered
    surface.blit(textobj, textrect) #txt on surface
    
#Put btn on screen
def put_button(text, fonttype, fontsize, fontcolor, padding, bgcolor, bordercolor, borderwidth, surface, x, y):
    font = set_font(fonttype, fontsize)
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

"""Initializing the screen and prepping"""
def game_start():
    global clock, screen, running, playing, paused
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(WINDOW_SIZE)  #window
    pygame.display.set_caption("Minotaur Maze Game")
    
"""Exit Program"""
def exit_game():
    global running
    running = False
    pygame.quit()

state = 'menu'  #menu, manual, playing
inventory_open = False

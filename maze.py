import pygame

WIDTH, HEIGHT = 800, 1000    #width and height of window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #window
pygame.display.set_caption("Minotaur Maze Game")

def main(): #Where all the code is going to go
    
    #CODE BEFORE STARTUP GOES HERE
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #CODE After STARTUP GOES HERE
    
    pygame.quit()
    
if __name__ == "__main__":  #so game is only run when wanted, __name__ = name of file
    main()

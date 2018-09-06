import pygame
from pygame import gfxdraw
from pygame.time import Clock

from life import Life

# Screen size
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

# Rectangle size
RECT_SIZE = 4

# Number of points
INITIAL_POINTS = 768

# Frames per second
FPS = 10

BLACK = (0, 0, 0)
WHITE = (155, 155, 255)

# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    clock = Clock()

    # create a surface on screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # create Life instance
    life = Life(screen, SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_POINTS, WHITE, RECT_SIZE)

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                life.toggle_clicked(pos)
        
        # Clear the screen and set the screen background
        screen.fill(BLACK)

        # Update life points
        life.update()

        # Update screen
        pygame.display.flip()

        clock.tick(FPS)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__== "__main__":
    # call the main function
    main()

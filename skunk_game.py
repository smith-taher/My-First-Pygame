# 1 - Import library
import pygame
#from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 1280, 720
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]

# 3 - Load images
player = pygame.image.load("resources/images/skunk.png")
map = pygame.image.load("resources/images/map.jpg")
#georgia = pygame.image.load("resources/images/georgia.png")
#colorado = pygame.image.load("resources/images/colorado.png")
#castle = pygame.image.load("resources/image/castle.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(width/map.get_width()+1):
        for y in range(height/map.get_height()+1):
            screen.blit(map,(x*100, y*100))
    #screen.blit(georgia,(470, 290))
    #screen.blit(colorado,(0, 0))
    # screen.blit(castle,(0, 30))
    # screen.blit(castle,(0, 135))
    # screen.blit(castle,(0, 240))
    # screen.blit(castle,(0, 345))
    screen.blit(player, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys[0] = False
                elif event.key == pygame.K_a:
                    keys[1] = False
                elif event.key == pygame.K_s:
                    keys[2] = False
                elif event.key == pygame.K-d:
                    keys[3] = False
    #9 - Move player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    elif keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
            # if it is quit the game
           


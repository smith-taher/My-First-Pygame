import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
        ball = pygame.image.load("resources/images/skunk.png").convert_alpha()
        screen.blit(ball, (self.x, self.y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load("resources/images/map.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main():

    # declare the size of the canvas
    width = 1280
    height = 720
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Skunk Game')

    # Game initialization
    ball = Ball(100, 100)
    BackGround = Background('background_image.png', [0, 0])

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    ball.speed_y = 5
                elif event.key == KEY_UP:
                    ball.speed_y = -5
                elif event.key == KEY_LEFT:
                    ball.speed_x = -5
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    ball.speed_y = 0
                elif event.key == KEY_UP:
                    ball.speed_y = 0
                elif event.key == KEY_LEFT:
                    ball.speed_x = 0
                elif event.key == KEY_RIGHT:
                    ball.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        ball.update()

        # Draw background
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Game display
        ball.render(screen)
        font = pygame.font.Font(None, 25)
        text = font.render('Get the Skunk to Georgia', True, (0, 0, 0))
        screen.blit(text, (500, 0))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()


# 1 - Import library
# import pygame
# #from pygame.locals import *

# # 2 - Initialize the game
# pygame.init()
# width, height = 1280, 720
# screen=pygame.display.set_mode((width, height))
# keys = [False, False, False, False]
# playerpos = [100, 100]

# # 3 - Load images
# player = pygame.image.load("resources/images/skunk.png")
# map = pygame.image.load("resources/images/map.jpg")
#georgia = pygame.image.load("resources/images/georgia.png")
#colorado = pygame.image.load("resources/images/colorado.png")
#castle = pygame.image.load("resources/image/castle.png")

# 4 - keep looping through
# while 1:
#     # 5 - clear the screen before drawing it again
#     screen.fill(0)
#     # 6 - draw the screen elements
#     for x in range(width/map.get_width()+1):
#         for y in range(height/map.get_height()+1):
#             screen.blit(map,(x*100, y*100))
#     #screen.blit(georgia,(470, 290))
#     #screen.blit(colorado,(0, 0))
#     # screen.blit(castle,(0, 30))
#     # screen.blit(castle,(0, 135))
#     # screen.blit(castle,(0, 240))
#     # screen.blit(castle,(0, 345))
#     screen.blit(player, playerpos)
#     # 7 - update the screen
#     pygame.display.flip()
#     # 8 - loop through the events
#     for event in pygame.event.get():
#         # check if the event is the X button 
#         if event.type==pygame.QUIT:
#             pygame.quit() 
#             exit(0) 
#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_w:
#                     keys[0] = True
#                 elif event.key == K_a:
#                     keys[1] = True
#                 elif event.key == K_s:
#                     keys[2] = True
#                 elif event.key == K_d:
#                     keys[3] = True
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_w:
#                     keys[0] = False
#                 elif event.key == pygame.K_a:
#                     keys[1] = False
#                 elif event.key == pygame.K_s:
#                     keys[2] = False
#                 elif event.key == pygame.K-d:
#                     keys[3] = False
#     #9 - Move player
#     if keys[0]:
#         playerpos[1] -= 5
#     elif keys[2]:
#         playerpos[1] += 5
#     elif keys[1]:
#         playerpos[0] -= 5
#     elif keys[3]:
#         playerpos[0] += 5
            # if it is quit the game
           


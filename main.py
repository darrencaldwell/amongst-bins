import pygame
from pygame.locals import *
import os 

os.environ['SDL_VIDEO_CENTERED'] = '1'
 
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen_height = 1080
screen_width = 1920 
screen=pygame.display.set_mode((screen_width, screen_height))

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = pygame.font.SysFont("comicsansms", 72)
 
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30

def main_menu():
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()

        screen.fill(blue)
        title=text_format('Pacifico.ttf', font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

                    


# class Player(pygame.sprite.Sprite):
#     #     self.surf = pygame.image.load('assets/bins/grey bin/grey_left.svg').convert()
#     #     self.rect = self.surf.get_rect()
#     def __init__(self): 
#         super(Player, self).__init__()
#         pygame.sprite.Sprite.__init__(self) 
#         self.image = pygame.image.load('assets/bins/grey bin/grey_left.svg').convert() 
#         # resize the image
#         self.image = pygame.transform.scale(self.image, (20, 30))
#         self.rect = self.image.get_rect() 

# pygame.init()


# screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
# player = Player()
# running = True

# while running:
#     # Look at every event in the queue
#     for event in pygame.event.get():
#         # Did the user hit a key?
#         if event.type == KEYDOWN:
#             # Was it the Escape key? If so, stop the loop.
#             if event.key == K_ESCAPE:
#                 running = False

#         # Did the user click the window close button? If so, stop the loop.
#         elif event.type == QUIT:
#             running = False

#     screen.fill((0, 0, 255))

#     player_center = (
#         (SCREEN_WIDTH-screen.get_width())/2,
#         (SCREEN_HEIGHT-screen.get_height())/2
#     ) 

#     screen.blit(player.image, player_center)
#     pygame.display.flip()

main_menu()
pygame.quit()
quit()

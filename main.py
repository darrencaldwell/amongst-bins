import pygame
 
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

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1920

class Player(pygame.sprite.Sprite):

    def __init__(self): 
        super(Player, self).__init__()
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('assets/bins/grey bin/grey_left.svg').convert() 
        self.image = pygame.transform.scale(self.image, (300, 400))
        self.rect = self.image.get_rect() 


pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
player = Player()
running = True

while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(player.image, (800,300))
    pygame.display.flip()


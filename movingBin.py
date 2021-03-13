import pygame
from pygame.locals import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1000
RED = (255, 0, 0)
GRAY = (150, 150, 150)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('assets/bins/grey bin/grey_left.svg')
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.rect = self.image.get_rect()
        self.rect.center = w//2, h//2

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


pygame.init()
w, h = 1080, 1000
screen = pygame.display.set_mode((w, h))
running = True
moving = False
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill(GRAY)
    screen.blit(player.image, player.rect)
    pygame.draw.rect(screen, RED, player.rect, 1)
    pygame.display.update()

pygame.quit()

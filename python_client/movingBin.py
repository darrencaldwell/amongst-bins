import pygame
import random

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
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
RED = (255, 0, 0)
GRAY = (150, 150, 150)


class Player(pygame.sprite.Sprite):

    def __init__(self, w, h):
        super(Player, self).__init__()
        self.image = pygame.image.load('../assets/bins/grey bin/grey_left.svg')
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('../assets/banana.png')
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (200, 300))
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH -500 , 1000),
                random.randint(200, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(0, 0)

    # Move the sprite based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#pygame.init()
#w, h = 1080, 1000
#screen = pygame.display.set_mode((w, h))
#ADDENEMY = pygame.USEREVENT + 1
#pygame.time.set_timer(ADDENEMY, 2000)
#running = True
#moving = False
#player = Player()
#enemies = pygame.sprite.Group()
#all_sprites = pygame.sprite.Group()
#all_sprites.add(player)
#
#while running:
#    for event in pygame.event.get():
#        if event.type == KEYDOWN:
#            if event.key == K_ESCAPE:
#                running = False
#        elif event.type == QUIT:
#            running = False
#        elif event.type == ADDENEMY:
#            new_enemy = Enemy()
#            enemies.add(new_enemy)
#            all_sprites.add(new_enemy)
#
#    pressed_keys = pygame.key.get_pressed()
#    player.update(pressed_keys)
#    enemies.update()
#    screen.fill(GRAY)
#
#    for entity in all_sprites:
#        screen.blit(entity.image, entity.rect)
#        pygame.draw.rect(screen, RED, entity.rect, 1)
#
#
#    if pygame.sprite.spritecollideany(player, enemies):
#        player.kill()
#        running = False
#
#    pygame.display.update()
#
#pygame.quit()

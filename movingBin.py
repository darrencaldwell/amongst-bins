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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def update(pressed_keys):
    if pressed_keys[K_UP]:
        rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        rect.move_ip(5, 0)

    if rect.left < 0:
        rect.left = 0
    elif rect.right > SCREEN_WIDTH:
        rect.right = SCREEN_WIDTH
    if rect.top <= 0:
        rect.top = 0
    elif rect.bottom >= SCREEN_HEIGHT:
        rect.bottom = SCREEN_HEIGHT


RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('assets/bins/grey bin/grey_left.svg')
img.convert()
img = pygame.transform.scale(img, (200, 200))
rect = img.get_rect()
rect.center = w//2, h//2
moving = False

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    update(pressed_keys)

    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()

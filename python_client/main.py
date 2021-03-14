#!/usr/bin/python3.4
import pygame, sys
import protocol
from movingBin import *
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Main Menu')

screen = pygame.display.set_mode((1280, 720),0,32)
font = pygame.font.SysFont(None, 20)

smallfont = pygame.font.SysFont('Corbel',35) 
color = (255,255,255) 
text = smallfont.render('quit' , True , color) 
text1  = smallfont.render('game' , True , color) 
text2  = smallfont.render('options' , True , color) 


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    # connect to server, get into game
    s = protocol.connect()

    w, h = 1080, 1000
    #pygame.time.set_timer(ADDENEMY, 2000)
    running = True
    moving = False
    player = Player(w, h)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
    #        elif event.type == ADDENEMY:
    #            new_enemy = Enemy()
    #            enemies.add(new_enemy)
    #            all_sprites.add(new_enemy)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.fill(GRAY)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            pygame.draw.rect(screen, RED, entity.rect, 1)

        pygame.display.update()
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()

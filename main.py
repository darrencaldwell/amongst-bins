import pygame
from pygame.locals import *
import os 

#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
# import pygame, sys
 
# # Setup pygame/window ---------------------------------------- #
# mainClock = pygame.time.Clock()
# from pygame.locals import *
# pygame.init()
# pygame.display.set_caption('main menu')
# screen = pygame.display.set_mode((500, 500),0,32)
 
# font = pygame.font.SysFont(None, 20)
 
# def draw_text(text, font, color, surface, x, y):
#     textobj = font.render(text, 1, color)
#     textrect = textobj.get_rect()
#     textrect.topleft = (x, y)
#     surface.blit(textobj, textrect)
 
# click = False
 
# def main_menu():
#     while True:
 
#         screen.fill((0,0,0))
#         draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
#         mx, my = pygame.mouse.get_pos()
 
#         button_1 = pygame.Rect(50, 100, 200, 50)
#         button_2 = pygame.Rect(50, 200, 200, 50)
#         if button_1.collidepoint((mx, my)):
#             if click:
#                 game()
#         if button_2.collidepoint((mx, my)):
#             if click:
#                 options()
#         pygame.draw.rect(screen, (255, 0, 0), button_1)
#         pygame.draw.rect(screen, (255, 0, 0), button_2)
 
#         click = False
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#             if event.type == MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     click = True
 
#         pygame.display.update()
#         mainClock.tick(60)
 
 

# main_menu()

import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 

text1  = smallfont.render('game' , True , color) 

text2  = smallfont.render('options' , True , color) 

def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

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
 

while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
                  
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 

            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 

            # if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40: 
            #     pygame.game()
            # if width/2 <= mouse[0] <= width/2+140 and height/2.5 <= mouse[1] <= height/2.5+40: 
            #     pygame.options()

    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 

    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/3+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/3,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/3, 140, 40]) 

    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2.5 <= mouse[1] <= height/2.5+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2.5,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2.5, 140, 40]) 


    # superimposing the text onto our button 
    screen.blit(text, (width/2+50,height/2)) 

    # superimposing the text onto our button 
    screen.blit(text1, (width/2+50,height/3)) 
      
    # superimposing the text onto our button 
    screen.blit(text2, (width/2+50,height/2.5)) 

    # updates the frames of the game 
    pygame.display.update() 


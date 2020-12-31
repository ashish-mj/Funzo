#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:52:45 2020

@author: ashish
"""

import pygame,sys,math,random
import pandas as pd




def draw():
    window.fill(white)
    
    display_word=""
    for letter in word:
        if letter in guess:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1,black)
    window.blit(text,(400,200))
    
    for letter in letters:
        if letter[3]:
            pygame.draw.circle(window,black,(letter[0],letter[1]),radius,3)
            text = font.render(letter[2], 1, black)
            window.blit(text,(letter[0]-text.get_width()/2,letter[1]-text.get_height()/2))
        
    window.blit(images[status],(150,100))
    pygame.display.update()



pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Hangman')
clock= pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
font = pygame.font.Font('freesansbold.ttf', 20)
word_font = pygame.font.Font('freesansbold.ttf', 30)

images=[]
for i in range(7):
    image= pygame.image.load("images/hangman"+str(i)+".png")
    images.append(image)

status = 0
radius = 20
gap = 15
letters=[]
start_x = round((800 -(radius*2+gap)*13)/2)
start_y = 400
A_asci = 65
words_list=["DEVELOPER","INDIA","GOOD","BRIDGE","TEMPERATURE","PYTHON","SPEAKER","GLORIOUS","ARENA"]
word=random.choice(words_list)
guess=[]

for i in range(26):
    x = start_x + gap*2 +((radius *2 +gap)*(i%13))
    y = start_y + ((i//13)) * (gap+radius*2)
    letters.append([x,y,chr(A_asci+i),True])



while True:
    
    clock.tick(60)
    draw()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                status=0
                guess=[]
                letters=[]
                word=random.choice(words_list)
                for i in range(26):
                    x = start_x + gap*2 +((radius *2 +gap)*(i%13))
                    y = start_y + ((i//13)) * (gap+radius*2)
                    letters.append([x,y,chr(A_asci+i),True])
                
        
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            
            for letter in letters:
                dis = math.sqrt((position[0]-letter[0])**2+(position[1]-letter[1])**2)
                if dis<radius:
                    letter[3]=False
                    guess.append(letter[2])
                    
                    if letter[2] not in word:
                        status+=1
    
    won = True
    for letter in word:
        if letter not in guess:
            won = False
            break
    if won:
        window.fill(white)
        text = word_font.render("YOU WON! ENTER SPACE TO START AGAIN",1,black)
        window.blit(text,(800/2-text.get_width()/2, 500/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
    if status==6:
        window.fill(white)
        text = word_font.render("YOU LOST! ENTER SPACE TO START AGAIN",1,black)
        window.blit(text,(800/2-text.get_width()/2, 500/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        
   
    

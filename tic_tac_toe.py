#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:50:04 2020

@author: ashish
"""

import pygame,sys


def check_winner(n):
    for row in board:
        for tile in row:
            if tile == n:
                continue
            else:
                break
        else:
            return True
        
    for col in range(3):
        for row in board:
            if row[col]==n:
                continue
            else:
                break
        else:
            return True
        
    for tile in range(3):
        if board[tile][tile]==n:
            continue
        else:
            break
    else:
        return True
    
    for tile in range(3):
        if board[tile][2-tile]==n:
            continue
        else:
            break
    else:
        return True
            



pygame.init()

window = pygame.display.set_mode((550,550))
pygame.display.set_caption('Tic-Tac-Toe')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

first = pygame.draw.rect(window, white, (25,25,150,150))
second = pygame.draw.rect(window, white,(200,25,150,150))
third = pygame.draw.rect(window, white,(375,25,150,150))

forth = pygame.draw.rect(window, white,(25,200,150,150))
fifth = pygame.draw.rect(window, white,(200,200,150,150))
sixth = pygame.draw.rect(window, white,(375,200,150,150))

seventh = pygame.draw.rect(window, white,(25,375,150,150))
eight = pygame.draw.rect(window, white,(200,375,150,150))
nine = pygame.draw.rect(window, white,(375,375,150,150))


font = pygame.font.Font('freesansbold.ttf', 21)
text1 = font.render('RECTANGLE WON , ENTER SPACE TO RESTART', True, green, blue)
textRect1 = text1.get_rect()
textRect1.center = (275, 550// 2)
text2 = font.render('CIRCLE WON , ENTER SPACE TO RESTART', True, green, blue)
textRect2 = text2.get_rect()
textRect2.center = (275, 550// 2)





player_turn = 'rect'

space = [[True,True,True],[True,True,True],[True,True,True]]

board = [[0,0,0],[0,0,0],[0,0,0]]

won = False

def tic_tac_toe():
    global won,first,second,third,forth,fifth,sixth,seventh,eight,nine
    global space,board,player_turn,text1,text2
    while True:
        
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    window.fill(black)
                    
                    first = pygame.draw.rect(window, white, (25,25,150,150))
                    second = pygame.draw.rect(window, white,(200,25,150,150))
                    third = pygame.draw.rect(window, white,(375,25,150,150))
    
                    forth = pygame.draw.rect(window, white,(25,200,150,150))
                    fifth = pygame.draw.rect(window, white,(200,200,150,150))
                    sixth = pygame.draw.rect(window, white,(375,200,150,150))
    
                    seventh = pygame.draw.rect(window, white,(25,375,150,150))
                    eight = pygame.draw.rect(window, white,(200,375,150,150))
                    nine = pygame.draw.rect(window, white,(375,375,150,150))
                    
                    space = [[True,True,True],[True,True,True],[True,True,True]]
                    board = [[0,0,0],[0,0,0],[0,0,0]]
                    player_turn="rect"
                    won=False
                
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                
                if won != True:
                    
                    if first.collidepoint(position) and space[0][0]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(50,50,100,100))
                            player_turn="circle"
                            board[0][0]=1
                        else:
                            pygame.draw.circle(window,green,(100,100),50)
                            player_turn="rect"
                            board[0][0]=2
                        space[0][0]=False
                    
                    if second.collidepoint(position) and space[0][1]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(225,50,100,100))
                            player_turn="circle"
                            board[0][1]=1
                        else:
                            pygame.draw.circle(window,green,(275,100),50)
                            player_turn="rect"
                            board[0][1]=2
                        space[0][1]=False    
                         
                    if third.collidepoint(position) and space[0][2]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(400,50,100,100))
                            player_turn="circle"
                            board[0][2]=1
                        else:
                            pygame.draw.circle(window,green,(450,100),50)
                            player_turn="rect"
                            board[0][2]=2
                        space[0][2]=False
                        
                    if forth.collidepoint(position) and space[1][0]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(50,225,100,100))
                            player_turn="circle"
                            board[1][0]=1
                        else:
                            pygame.draw.circle(window,green,(100,275),50)
                            player_turn="rect"
                            board[1][0]=2
                        space[1][0]=False
                        
                    if fifth.collidepoint(position) and space[1][1]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(225,225,100,100))
                            player_turn="circle"
                            board[1][1]=1
                        else:
                            pygame.draw.circle(window,green,(275,275),50)
                            player_turn="rect"
                            board[1][1]=2
                        space[1][1]=False
                        
                    if sixth.collidepoint(position) and space[1][2]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(400,225,100,100))
                            player_turn="circle"
                            board[1][2]=1
                        else:
                            pygame.draw.circle(window,green,(450,275),50)
                            player_turn="rect"
                            board[1][2]=2
                        space[1][2]=False
                         
                    if seventh.collidepoint(position) and space[2][0]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(50,400,100,100))
                            player_turn="circle"
                            board[2][0]=1
                        else:
                            pygame.draw.circle(window,green,(100,450),50)
                            player_turn="rect"
                            board[2][0]=2
                        space[2][0]=False
                    
                    if eight.collidepoint(position) and space[2][1]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(225,400,100,100))
                            player_turn="circle"
                            board[2][1]=1
                        else:
                            pygame.draw.circle(window,green,(275,450),50)
                            player_turn="rect"
                            board[2][1]=2
                            space[2][1]=False
                        
                    if nine.collidepoint(position) and space[2][2]:
                        if player_turn=="rect":
                            pygame.draw.rect(window,red,(400,400,100,100))
                            player_turn="circle"
                            board[2][2]=1
                        else:
                            pygame.draw.circle(window,green,(450,450),50)
                            player_turn="rect"
                            board[2][2]=2
                        space[2][2]=False
                    
                
                    if check_winner(1):
                        won=True
                        print("Rectangle Won")
                        window.blit(text1, textRect1)
                    if check_winner(2):
                        won=True
                        print("Circle Won")
                        window.blit(text2, textRect2)
                
                    
                
                
        
        pygame.display.update()
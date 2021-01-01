#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:15:24 2020

@author: ashish
"""

import pygame,sys,random

def ball_movement(pong_sound,score_sound):
    
    global ball_speed_x,ball_speed_y,player_score,cpu_score,score_time
    
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y
    
    if ball.top <=0 or ball.bottom>= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
        
    if ball.left <=0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.right>= screen_width:
        pygame.mixer.Sound.play(score_sound)
        cpu_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
        
    if ball.colliderect(cpu) and  ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
 
def player_movement():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height    
    
def cpu_movement():
    if cpu.top < ball.y:
        cpu.top += cpu_speed
    if cpu.bottom > ball.y:
        cpu.bottom -= cpu_speed
    if cpu.top <= 0:
        cpu.top=0
    if cpu.bottom >=screen_height:
        cpu.bottom =screen_height
        
def ball_restart(screen,game_font):
    global ball_speed_x,ball_speed_y, score_time
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2,screen_height/2)
    
    if current_time - score_time < 700:
        three = game_font.render("3",False, border)
        screen.blit(three,(screen_width/2-10,screen_height/2+20))
        
    if 700 < current_time - score_time < 1400:
        two = game_font.render("2",False, border)
        screen.blit(two,(screen_width/2-10,screen_height/2+20))
        
    if 1400 < current_time - score_time < 2100:
        one = game_font.render("1",False, border)
        screen.blit(one,(screen_width/2-10,screen_height/2+20))
        
    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        ball_speed_y = 7* random.choice((1,-1))
        ball_speed_x = 7* random.choice((1,-1))
        score_time = None


#pygame.init()
#clock = pygame.time.Clock()


screen_width = 1260
screen_height = 600


ball = pygame.Rect(screen_width/2-15,screen_height/2-15,30,30)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
cpu = pygame.Rect(10,screen_height/2-70,10,140)

############################################
green = (0, 133, 35)
border = (200,200,200)
white = (255,255,255) 
########################################

ball_speed_x = 6 * random.choice((1,-1))
ball_speed_y = 6 * random.choice((1,-1))
player_speed, cpu_speed = 0,7


player_score = 0
cpu_score = 0


score_time = True


def ping_pong():
    print("STARTED PING_PONG")
    
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Ping Pong')
    
    game_font = pygame.font.Font("freesansbold.ttf",32)
    
    pong_sound = pygame.mixer.Sound("static/audio/pong.ogg")
    score_sound = pygame.mixer.Sound("static/audio/score.ogg")


    run=True
    global player_speed
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("EXIT PING_PONG")
                run=False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed -= 6
                if event.key == pygame.K_DOWN:
                    player_speed += 6
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed += 6
                if event.key == pygame.K_DOWN:
                    player_speed -= 6
        
        ball_movement(pong_sound,score_sound)
        player_movement()
        cpu_movement()
        
        screen.fill(green)
        pygame.draw.rect(screen,white,player)
        pygame.draw.rect(screen,white,cpu)
        pygame.draw.ellipse(screen,white,ball)
        pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))
        
        if score_time:
            ball_restart(screen,game_font)
        
        player_text = game_font.render(f"{player_score}",False,border)
        screen.blit(player_text,(660,290))
        
        cpu_text = game_font.render(f"{cpu_score}",False,border)
        screen.blit(cpu_text,(583,290))
        
        CPU = game_font.render("CPU",False,border)
        screen.blit(CPU,(10,10))
        
        ashish = game_font.render("Player",False,border)
        screen.blit(ashish,(screen_width-130,10))
        
        
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
        
                
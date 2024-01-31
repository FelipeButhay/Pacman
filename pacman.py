import pygame
import math
import random
import pacman_aux as aux 
import pandas as pd
import pacman_ai as ai

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((aux.screen_x, aux.screen_y))
pygame.display.set_caption("PacMan")

grid_save, grid, power_ups, empty, blocks, pacman_s, ghost_s, semi_blocks, targets, sq, gap = aux.interpreter()

pacman = aux.PacMan([pacman_s[0][0]+.5, pacman_s[0][1]+.5], (0,-1))
red_g  = aux.Ghost([-10, -10], (0,-1), 0)
pink_g = aux.Ghost([-10, -10], (0,-1), 1)
blue_g = aux.Ghost([-10, -10], (0,-1), 2)
oran_g = aux.Ghost([-10, -10], (0,-1), 3)
ghosts = [red_g, pink_g, blue_g, oran_g]
n = 0
ticks = 0
v = 0

dots = []
for x in empty:
    dots.append(aux.Dot(x))
    
bigdots = []
for x in power_ups:
    bigdots.append(aux.BigDot(x))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    n+=1
    if n%20==0:
        ticks +=1
    if n%(300):
        aux.spawn(ghosts, grid_save)
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman.facing = ( 0, -1)
    if keys[pygame.K_DOWN]:
        pacman.facing = ( 0,  1)
    if keys[pygame.K_LEFT]:
        pacman.facing = (-1,  0)
    if keys[pygame.K_RIGHT]:
        pacman.facing = ( 1,  0)
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        v = 1/15
            
    screen.fill("black")
    aux.draw_level(screen, grid_save)
    for x in dots[:]:
        if x.check(pacman):
            dots.remove(x)
        x.draw(sq, screen)
        
    for x in bigdots:
        if x.check(pacman):
            bigdots.remove(x)
            for y in ghosts:
                y.eatable = True
                y.eat_time = 8
                if not y.dead:
                    y.facing = (-y.facing[0], -y.facing[1])
        x.draw(sq, screen)
        
    for x in ghosts:
        if x.check(pacman):
            if x.eatable:
                x.eatable = False
                x.eat_time = 0
                x.dead = True
            elif not x.dead and not x.eatable:
                playing = False
                print("PERDISTE, PEDAZO DE MOGO")
                
        if x.eat_time > 0:
            x.eat_time -= 1/60
        else:
            x.eatable = False
        if x.pos != [-10, -10]:
            x.move(grid, blocks, pacman, targets, grid_save, semi_blocks, ghosts, n)
        x.draw(screen, ticks)
        
    pacman.move(v, grid, [*blocks, *semi_blocks])
    pacman.draw(screen, ticks)
    
    if len(dots) == 0:
        playing = False
        print("GANASTE")
    
    pygame.display.update()
    clock.tick(60)
    
while not playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
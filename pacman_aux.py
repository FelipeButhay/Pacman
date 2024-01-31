import pygame
import os
import pacman_ai as ai
import random

screen_x = 1600
screen_y = 900
# while __name__ == "__main__":
#     try:
#         resolution = input("resolution (x,y format): ").split(",")
#         screen_x = int(resolution[0])
#         screen_y = int(resolution[1]) 
#         break
#     except:
#         pass

#pacman
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')
pm_up    = pygame.image.load(f"{direc}/assets/pacman/pm_u_c.png"), pygame.image.load(f"{direc}/assets/pacman/pm_u_o.png")
pm_left  = pygame.image.load(f"{direc}/assets/pacman/pm_l_c.png"), pygame.image.load(f"{direc}/assets/pacman/pm_l_o.png")
pm_right = pygame.image.load(f"{direc}/assets/pacman/pm_r_c.png"), pygame.image.load(f"{direc}/assets/pacman/pm_r_o.png")
pm_down  = pygame.image.load(f"{direc}/assets/pacman/pm_d_c.png"), pygame.image.load(f"{direc}/assets/pacman/pm_d_o.png")

#red
gr_up    = pygame.image.load(f"{direc}/assets/ghost/ghost_red_up_1.gif"),       pygame.image.load(f"{direc}/assets/ghost/ghost_red_up_2.gif")
gr_left  = pygame.image.load(f"{direc}/assets/ghost/ghost_red_left_1.gif"),     pygame.image.load(f"{direc}/assets/ghost/ghost_red_left_2.gif")
gr_right = pygame.image.load(f"{direc}/assets/ghost/ghost_red_right_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_red_right_2.gif")
gr_down  = pygame.image.load(f"{direc}/assets/ghost/ghost_red_down_1.gif"),     pygame.image.load(f"{direc}/assets/ghost/ghost_red_down_2.gif")

#pink
gp_up    = pygame.image.load(f"{direc}/assets/ghost/ghost_pink_up_1.gif"),      pygame.image.load(f"{direc}/assets/ghost/ghost_pink_up_2.gif")
gp_left  = pygame.image.load(f"{direc}/assets/ghost/ghost_pink_left_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_pink_left_2.gif")
gp_right = pygame.image.load(f"{direc}/assets/ghost/ghost_pink_right_1.gif"),   pygame.image.load(f"{direc}/assets/ghost/ghost_pink_right_2.gif")
gp_down  = pygame.image.load(f"{direc}/assets/ghost/ghost_pink_down_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_pink_down_2.gif")

#blue
gb_up    = pygame.image.load(f"{direc}/assets/ghost/ghost_blue_up_1.gif"),      pygame.image.load(f"{direc}/assets/ghost/ghost_blue_up_2.gif")
gb_left  = pygame.image.load(f"{direc}/assets/ghost/ghost_blue_left_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_blue_left_2.gif")
gb_right = pygame.image.load(f"{direc}/assets/ghost/ghost_blue_right_1.gif"),   pygame.image.load(f"{direc}/assets/ghost/ghost_blue_right_2.gif")
gb_down  = pygame.image.load(f"{direc}/assets/ghost/ghost_blue_down_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_blue_down_2.gif")

#orange
go_up    = pygame.image.load(f"{direc}/assets/ghost/ghost_orange_up_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_orange_up_2.gif")
go_left  = pygame.image.load(f"{direc}/assets/ghost/ghost_orange_left_1.gif"),  pygame.image.load(f"{direc}/assets/ghost/ghost_orange_left_2.gif")
go_right = pygame.image.load(f"{direc}/assets/ghost/ghost_orange_right_1.gif"), pygame.image.load(f"{direc}/assets/ghost/ghost_orange_right_2.gif")
go_down  = pygame.image.load(f"{direc}/assets/ghost/ghost_orange_down_1.gif"),  pygame.image.load(f"{direc}/assets/ghost/ghost_orange_down_2.gif")

#dead
gdead_up    = pygame.image.load(f"{direc}/assets/ghost/ghost_dead_up.gif")
gdead_left  = pygame.image.load(f"{direc}/assets/ghost/ghost_dead_left.gif")
gdead_right = pygame.image.load(f"{direc}/assets/ghost/ghost_dead_right.gif")
gdead_down  = pygame.image.load(f"{direc}/assets/ghost/ghost_dead_down.gif")

#eatable
geat     = pygame.image.load(f"{direc}/assets/ghost/ghost_eatable_1.gif"),     pygame.image.load(f"{direc}/assets/ghost/ghost_eatable_2.gif")
geat_end = pygame.image.load(f"{direc}/assets/ghost/ghost_eatable_end_1.gif"), pygame.image.load(f"{direc}/assets/ghost/ghost_eatable_end_2.gif")

corner_a = pygame.image.load(f"{direc}/assets/corners/A_corner.png")
corner_b = pygame.image.load(f"{direc}/assets/corners/B_corner.png")
corner_d = pygame.image.load(f"{direc}/assets/corners/D_corner.png")
corner_e = pygame.image.load(f"{direc}/assets/corners/E_corner.png")
corner_f = pygame.image.load(f"{direc}/assets/corners/F_corner.png")
corner_g = pygame.image.load(f"{direc}/assets/corners/G_corner.png")
corner_h = pygame.image.load(f"{direc}/assets/corners/H_corner.png")
door = pygame.image.load(f"{direc}/assets/door.png")
corners = [corner_a, corner_b, corner_d, corner_e, corner_f, corner_g, corner_h, door]

all_sprites = [pm_up, pm_left, pm_right, pm_down, gr_up, gr_left, gr_right, gr_down, gp_up, gp_left, gp_right, gp_down,
               gb_up, gb_left, gb_right, gb_down,go_up, go_left, go_right, go_down, geat, geat_end, [gdead_up, gdead_left, gdead_right, gdead_down]]

def corner_id(grid_save, corner_checks, x, y):
    corner_ifs = [False, False, False]
    for z in range(0,3):
        try:
            if x + corner_checks[z][0] == -1 or y + corner_checks[z][1] == -1:
                continue
            corner_ifs[z] = (grid_save[x + corner_checks[z][0]][y + corner_checks[z][1]] == "b")
        except:
            pass
                    
    if corner_ifs == [False, False, False]:
        return corners[0]
    if corner_ifs == [False, False, True]:
        return corners[1]
    if corner_ifs == [False, True, False]:
        return corners[0]
    if corner_ifs == [False, True, True]:
        return corners[1]
    if corner_ifs == [True, False, False]:
        return corners[3]
    if corner_ifs == [True, False, True]:
        return corners[4]
    if corner_ifs == [True, True, False]:
        return corners[3]
    if corner_ifs == [True, True, True]:
        return corners[6]

def interpreter():
    with open(f"{direc}\\lvl\\lvl.txt", "r", encoding = "UTF-8") as file:
        grid_str = file.read().split("\n")
    grid_save = []
    for x in grid_str:
        grid_save.append(",".join(x).split(","))
        
    power_ups = []    
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "e":
                grid_save[xx][yy] = " "
                power_ups.append((xx, yy))
                
    blocks = []    
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "b":
                blocks.append((xx, yy))
                
    pacman_s = []
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "p":
                pacman_s.append((xx, yy))
    
    ghost_s = []
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "g":
                ghost_s.append((xx, yy))
                
    semi_blocks = []
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "d":
                semi_blocks.append((xx, yy))
                
    targets = []
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y == "t":
                targets.append((xx, yy))
        
    grid = (len(grid_save), len(grid_save[0]))
    ratio = screen_x/screen_y
    if grid[0] >= grid[1]*ratio:
        sq = (screen_x*.9 + .99)//grid[0]
        print(screen_x, screen_y*ratio)
    else:
        sq = (screen_y*.9 + .99)//grid[1]
    x_gap = (screen_x-sq*grid[0])*0.5
    y_gap = (screen_y-sq*grid[1])*0.5
    gap = x_gap, y_gap
    
    empty = {(x,y) for x in range(0, grid[0]) for y in range(0, grid[1])}
    for x in (blocks, pacman_s, ghost_s, semi_blocks, power_ups):
        xs = set(x)
        empty = empty.difference(xs)
        
    return grid_save, grid, power_ups, empty, blocks, pacman_s, ghost_s, semi_blocks, targets, sq, gap
    
def draw_level(screen, grid_save):
    for x in range(0, len(grid_save)):
        for y in range(0, len(grid_save[0])):
            sq_size = (sq, sq)
            sq_position = (gap[0]+x*sq, gap[1]+y*sq)
    
            if grid_save[x][y] == " ":
                pygame.draw.rect(screen, "black", (*sq_position, *sq_size))
            elif grid_save[x][y] == "b": # block
                # up left
                UL_corner_checks = ((-1, 0), (-1, -1), (0, -1))
                UL_corner = corner_id(grid_save, UL_corner_checks, x, y)
                UL_corner = pygame.transform.rotate(UL_corner, 0)
                screen.blit(UL_corner, sq_position)
                
                # up right
                UR_corner_checks = ((0,-1), (1, -1), (1, 0))
                UR_corner = corner_id(grid_save, UR_corner_checks, x, y)
                UR_corner = pygame.transform.rotate(UR_corner, 270)
                screen.blit(UR_corner, (sq_position[0]+sq/2, sq_position[1]))
                
                # down left
                DR_corner_checks = ((0, 1), (-1, 1), (-1, 0))
                DR_corner = corner_id(grid_save, DR_corner_checks, x, y)
                DR_corner = pygame.transform.rotate(DR_corner, 90)
                screen.blit(DR_corner, (sq_position[0], sq_position[1]+sq/2))
                
                # down right
                DL_corner_checks = ((1, 0), (1, 1), (0, 1))
                DL_corner = corner_id(grid_save, DL_corner_checks, x, y)
                DL_corner = pygame.transform.rotate(DL_corner, 180)
                screen.blit(DL_corner, (sq_position[0]+sq/2, sq_position[1]+sq/2))
            
                # pygame.draw.rect(screen, (80, 20, 250), (*sq_position, *sq_size))
            elif grid_save[x][y] == "d": # ghost door
                try:
                    if "db".find(grid_save[x][y+1]) != -1 or "db".find(grid_save[x][y-1]) != -1:
                        screen.blit(pygame.transform.rotate(corners[-1]), sq_position)
                    elif "db".find(grid_save[x+1][y]) != -1 or "db".find(grid_save[x-1][y]) != -1: 
                        screen.blit(corners[-1], sq_position)
                except:
                    pass
                # pygame.draw.rect(screen, (80, 20, 250), (sq_position[0], sq_position[1]+sq_size[1]*.4, sq_size[0], sq_size[1]*.2))

sq, gap = interpreter()[-2:]
fix_pos = lambda pos: (pos[0]*sq + gap[0], pos[1]*sq + gap[1])
fix_center = lambda pos: (int(pos[0])+.5, int(pos[1])+.5)

for xx, x in enumerate(all_sprites):
    all_sprites[xx] = list(all_sprites[xx])
    for yy, y in enumerate(x):
        all_sprites[xx][yy] = pygame.transform.scale(y, (sq*.8, sq*.8))
        
for xx, x in enumerate(corners):
    corners[xx] = pygame.transform.scale(x, (sq*.5, sq*.5))
corners[-1] = pygame.transform.scale(corners[-1], (sq,sq))
        
pacman_sprites    = all_sprites[:4]

g_red_sprites     = all_sprites[4:8]
g_pink_sprites    = all_sprites[8:12]
g_blue_sprites    = all_sprites[12:16]
g_orange_sprites  = all_sprites[16:20]
g_sprites         = (g_red_sprites, g_pink_sprites, g_blue_sprites, g_orange_sprites)

g_dead_sprites    = all_sprites[-1]
g_eatable_sprites = all_sprites[20:22]

facings = ((0,-1), (-1,0), (1,0), (0,1))

def spawn(ghosts, grid_save):
    for x in ghosts:
        if x.pos == [-10, -10]:
            for yy, y in enumerate(grid_save):
                if "g" in y:
                    x.pos = [yy, y.index("g")]
                    break
            break

class PacMan:
    def __init__(self, pos, facing):
        self.pos = list(pos)
        self.facing = facing
        self.rect = None
        self.sprite = None
    
    def move(self, v, grid, blocks):
        self.pos[0] += self.facing[0]*v
        self.pos[0] %= grid[0]
        self.pos[1] += self.facing[1]*v
        self.pos[1] %= grid[1]
        if (int(self.pos[0]+.5*self.facing[0]), int(self.pos[1]+.5*self.facing[1])) in blocks:
            self.pos[0] -= self.facing[0]*v
            self.pos[1] -= self.facing[1]*v        
        
        if self.facing[0] == 0:#veritcal
            self.pos[0] = int(self.pos[0])+.5
        else:#horizontal
            self.pos[1] = int(self.pos[1])+.5
        
    def draw(self, screen, tick):
        self.sprite = pacman_sprites[facings.index(self.facing)][tick%2]
        self.rect = self.sprite.get_rect(center = fix_pos(self.pos))
        screen.blit(self.sprite, self.rect)
    
class Ghost:
    def __init__(self, pos, facing, colour):
        self.pos = list(pos)
        self.facing = facing
        self.colour = colour #numero del 0-3 (indx de la lista)
        self.v = 12/300
        self.eatable = False
        self.eat_time = 0
        self.dead = False
        
    def move(self, grid, blocks, pacman, targets, grid_save, semi_blocks, ghosts, n):
        if self.pos == [-1, -1]:
            return None
        
        if n%int(.3/self.v) == 0 and not self.dead:
            if grid_save[int(self.pos[0])][int(self.pos[1])] == "g":
                self.facing = ai.behaviour(self.facing, self.pos, pacman, ghosts, blocks, grid_save, self.colour, self.eatable, self.dead)
            else:
                self.facing = ai.behaviour(self.facing, self.pos, pacman, ghosts, [*blocks, *semi_blocks], grid_save, self.colour, self.eatable, self.dead)
        elif n%int(.3/self.v) == 0 and self.dead:
            self.facing, last_n = ai.path_finder(self.pos, self.facing, grid)
            if last_n == 0:
                self.dead = False
                self.facing = (-self.facing[0], -self.facing[1])
            
        self.pos[0] += self.facing[0]*self.v
        self.pos[0] %= grid[0]
        self.pos[1] += self.facing[1]*self.v
        self.pos[1] %= grid[1]
        
        if (int(self.pos[0]+.5*self.facing[0]), int(self.pos[1]+.5*self.facing[1])) in blocks:
            self.pos[0] -= self.facing[0]*self.v
            self.pos[1] -= self.facing[1]*self.v        
        
        if self.facing[0] == 0:#veritcal
            self.pos[0] = int(self.pos[0])+.5
        else:#horizontal
            self.pos[1] = int(self.pos[1])+.5
    
    def check(self, pacman):
        return (int(pacman.pos[0]), int(pacman.pos[1])) == (int(self.pos[0]), int(self.pos[1]))
        
    def draw(self, screen, tick):
        if not self.eatable and not self.dead:
            self.sprite = g_sprites[self.colour][facings.index(self.facing)][tick%2]
                
        if self.eatable:
            if tick%4 > 1 and self.eat_time < 3:
                self.sprite = g_eatable_sprites[1][tick%2]
            else:
                self.sprite = g_eatable_sprites[0][tick%2]
             
        if self.dead:
            self.sprite = g_dead_sprites[facings.index(self.facing)]
                
        self.rect = self.sprite.get_rect(center = fix_pos(self.pos))
        screen.blit(self.sprite, self.rect)
    
class Dot:
    def __init__(self, position):
        self.pos = position
        
    def check(self, pacman):
        return (int(pacman.pos[0]), int(pacman.pos[1])) == self.pos
            
    def draw(self, sq, screen):
        pygame.draw.circle(screen, (231, 218, 109), fix_pos(fix_center(self.pos)), sq*.1)
        
class BigDot(Dot):
    def __init__(self, position):
        super().__init__(position)
        
    def draw(self, sq, screen):
        pygame.draw.circle(screen, (231, 218, 109), fix_pos(fix_center(self.pos)), sq*.2)
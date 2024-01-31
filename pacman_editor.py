import pygame
import os
import pandas as pd
from datetime import datetime

# El simbolo de pacman representa donde spawnea el pacman
# El fantasma rojo es dondw spawnean los fantasman
# El fantasma celeste es un bloque que solo los fantasmas pueden atravesar
# El bloque violeta es un bloque que nadie puede pasar
# El punto amarillo es aquel que come el pacman para poder comer fantasmas

# defs
def write(text, x, y, colour, size):
    font = pygame.font.Font(f"{direc}/assets/CONSOLA.TTF", size)
    img = font.render(str(text), True, colour)
    screen.blit(img, (x,y))

# elegir tamaño de la ventana
screen_x = 1920
screen_y = 1080
while False:
    try:
        resolution = input("resolution (x,y format): ").split(",")
        screen_x = int(resolution[0])
        screen_y = int(resolution[1]) 
        break
    except:
        pass

# inicializacion basica
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("PacMan Editor")

# algunos sprites
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')
corner_a = pygame.image.load(f"{direc}/assets/corners/A_corner.png")
corner_b = pygame.image.load(f"{direc}/assets/corners/B_corner.png")
corner_d = pygame.image.load(f"{direc}/assets/corners/D_corner.png")
corner_e = pygame.image.load(f"{direc}/assets/corners/E_corner.png")
corner_f = pygame.image.load(f"{direc}/assets/corners/F_corner.png")
corner_g = pygame.image.load(f"{direc}/assets/corners/G_corner.png")
corner_h = pygame.image.load(f"{direc}/assets/corners/H_corner.png")
corners = [corner_a, corner_b, corner_d, corner_e, corner_f, corner_g, corner_h]

gr_right = pygame.image.load(f"{direc}/assets/ghost/ghost_red_right_1.gif"),    pygame.image.load(f"{direc}/assets/ghost/ghost_red_right_2.gif")
gb_right = pygame.image.load(f"{direc}/assets/ghost/ghost_blue_right_1.gif"),   pygame.image.load(f"{direc}/assets/ghost/ghost_blue_right_2.gif")
pm_right = pygame.image.load(f"{direc}/assets/pacman/pm_r_c.png"),              pygame.image.load(f"{direc}/assets/pacman/pm_r_o.png")

up_left    = [corner_a, corner_b, corner_d, corner_e, corner_f, corner_g, corner_h]
up_right   = [pygame.transform.rotate(x,  90) for x in up_left]
down_left  = [pygame.transform.rotate(x, 270) for x in up_left]
down_right = [pygame.transform.rotate(x, 180) for x in up_left]

# variables lol
write_xy = {"x": ["1"], "y": ["1"]}
BLANK = ""

rel_size = 1
rel_pos_save = [0, 0]
rel_pos_in   = [0, 0]
rel_pos      = [0, 0]
mouse = [False for x in range(0,3)]

selected_coord = (screen_x*.04, screen_y*.04, screen_x*.22, screen_y*.07), "x"
selected_block = 0

grid_save = []
grid  = None
ratio = 1

click_rect = lambda pos, size, mouse_pos: (pos[0]<mouse_pos[0]<(pos[0]+size[0])) and (pos[1]<mouse_pos[1]<(pos[1]+size[1]))

blocks = () #ghost_spawner, block, big, dot
                    
def corner_id(grid_save, corner_checks, x, y, sq):
    corner_ifs = [False, False, False]
    for z in range(0,3):
        try:
            corner_ifs[z] = (grid_save[x + corner_checks[z][0]][y + corner_checks[z][1]] == "b")
        except:
            pass
                    
    for zz, z in enumerate(corners):
        corners[zz] = pygame.transform.scale(z, (sq*.5+1, sq*.5+1))
                    
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEWHEEL:
            # detecto la rueda del mouse
            rel_size += (event.dict["y"]*rel_size)/10
        if event.type == pygame.KEYDOWN:
            # detecto algunas teclas
            if event.dict["unicode"].isnumeric():
                write_xy[selected_coord[1]].append(event.dict["unicode"])
            if event.dict["unicode"] == "\x08":
                try:
                    write_xy[selected_coord[1]].pop(-1)
                except:
                    pass
                
            if event.dict["scancode"] == 82:
                selected_block -= 1
            if event.dict["scancode"] == 81:
                selected_block += 1
                
            if event.dict["unicode"] == "x":
                selected_coord = (screen_x*.04, screen_y*.04, screen_x*.22, screen_y*.07), "x"
            if event.dict["unicode"] == "y":
                selected_coord = (screen_x*.04, screen_y*.11, screen_x*.22, screen_y*.07), "y"
                
            if event.dict["unicode"] == "\r":
                try:
                    grid = (int(BLANK.join(write_xy['x'])), int(BLANK.join(write_xy['y'])))
                    ratio = grid[0]/grid[1]
                    
                    # changing x
                    if grid[0] > len(grid_save):   # hay que agregar
                        for x in range(0, grid[0] - len(grid_save)):
                            grid_save.append([])
                            for y in range(0, grid[0]):
                                grid_save[-1].append(" ")
                                
                    elif grid[0] < len(grid_save): # hay que sacar
                        for x in range(0, len(grid_save) - grid[0]):
                            grid_save.pop(-1)
                            
                    # changing y
                    if grid[1] > len(grid_save[0]):   # hay que agregar
                        for x in range(0, len(grid_save)):
                            for y in range(0, grid[1] - len(grid_save[x])):
                                grid_save[x].append(" ")
                            
                    elif grid[1] < len(grid_save[0]): # hay que sacar
                        for x in range(0, len(grid_save)):
                            for y in range(0, len(grid_save[x][:]) - grid[1]):
                                grid_save[x].pop(-1)
                    
                except ValueError:
                    grid  = None
    
    mouse_save = mouse
    mouse      = pygame.mouse.get_pressed()
    mouse_pos  = pygame.mouse.get_pos()
     
    # mover la visulizaion del canvas (copiado de mi simulacion orbital)       
    if mouse[2] and not mouse_save[2]:
        rel_pos_in[0] = mouse_pos[0]
        rel_pos_in[1] = mouse_pos[1]
        rel_pos_save  = tuple(rel_pos) 
        
    if mouse[2]:
        rel_pos[0] = mouse_pos[0] - rel_pos_in[0] + rel_pos_save[0]
        rel_pos[1] = mouse_pos[1] - rel_pos_in[1] + rel_pos_save[1]
    
    # sacando algunos datukis
    canvas_size = screen_x*.6*rel_size, screen_x*.6/ratio*rel_size
    canvas = (screen_x*.3 + rel_pos[0] + (screen_x*.7-canvas_size[0])/2, rel_pos[1] +(screen_y-canvas_size[1])/2, *canvas_size)
    
    # dibujando otras cosillas
    screen.fill(tuple(40 for x in range(0,3)))
    
    if grid != None:
        pygame.draw.rect(screen, tuple(230 for x in range(0,3)), canvas)
        for x in range(0, grid[0]):
            for y in range(0, grid[1]):
                sq_position = (canvas[0]+1+(canvas[2]/grid[0])*x, canvas[1]+1+(canvas[3]/grid[1])*y)
                sq_size = (canvas[2]/grid[0]-2, canvas[3]/grid[1]-2)
                sq = sq_size[0]
            
                if grid_save[x][y] == " ":
                    pygame.draw.rect(screen, "black", (*sq_position, *sq_size))
                elif grid_save[x][y] == "p":
                    pygame.draw.rect(screen, "black", (*sq_position, *sq_size))
                    screen.blit(pygame.transform.scale(pm_right[0], sq_size), sq_position)
                elif grid_save[x][y] == "g":
                    screen.blit(pygame.transform.scale(gr_right[1], sq_size), sq_position)
                elif grid_save[x][y] == "b":
                    # up left
                    UL_corner_checks = ((-1, 0), (-1, -1), (0, -1))
                    UL_corner = corner_id(grid_save, UL_corner_checks, x, y, sq)
                    UL_corner = pygame.transform.rotate(UL_corner, 0)
                    screen.blit(UL_corner, sq_position)
                
                    # up right
                    UR_corner_checks = ((0,-1), (1, -1), (1, 0))
                    UR_corner = corner_id(grid_save, UR_corner_checks, x, y, sq)
                    UR_corner = pygame.transform.rotate(UR_corner, 270)
                    screen.blit(UR_corner, (sq_position[0]+sq/2, sq_position[1]))
                
                    # down left
                    DR_corner_checks = ((0, 1), (-1, 1), (-1, 0))
                    DR_corner = corner_id(grid_save, DR_corner_checks, x, y, sq)
                    DR_corner = pygame.transform.rotate(DR_corner, 90)
                    screen.blit(DR_corner, (sq_position[0], sq_position[1]+sq/2))
                
                    # down right
                    DL_corner_checks = ((1, 0), (1, 1), (0, 1))
                    DL_corner = corner_id(grid_save, DL_corner_checks, x, y, sq)
                    DL_corner = pygame.transform.rotate(DL_corner, 180)
                    screen.blit(DL_corner, (sq_position[0]+sq/2, sq_position[1]+sq/2))
            
                    # pygame.draw.rect(screen, (80, 20, 250), (*sq_position, *sq_size))
                elif grid_save[x][y] == "e":
                    pygame.draw.rect(screen, "black", (*sq_position, *sq_size))
                    pygame.draw.circle(screen, (231, 218, 109), (sq_position[0]+sq_size[0]/2, sq_position[1]+sq_size[1]/2), sq_size[0]/6)
                elif grid_save[x][y] == "d":
                    screen.blit(pygame.transform.scale(gb_right[1], sq_size), sq_position)
                
                if mouse[0] and click_rect(sq_position, sq_size, mouse_pos):
                    match selected_block%4:
                        case 0:
                            grid_save[x][y] = "p"
                        case 1: 
                            grid_save[x][y] = "g"
                        case 2:
                            grid_save[x][y] = "b"
                        case 3:
                            grid_save[x][y] = "e"

                if mouse[2] and click_rect(sq_position, sq_size, mouse_pos) and selected_block%4 != 1:
                    grid_save[x][y] = " "
                if mouse[2] and click_rect(sq_position, sq_size, mouse_pos) and selected_block%4 == 1:
                    grid_save[x][y] = "d"
    # panel lateral
    pygame.draw.rect(screen, tuple(255 for x in range(0,3)), (0,0, screen_x*.3, screen_y))
    pygame.draw.rect(screen, tuple( 40 for x in range(0,3)), selected_coord[0])
    
    write(">", screen_x*.03, screen_y*(.36 + .16*(selected_block%4)), tuple( 40 for x in range(0,3)), int(screen_y*.08+.5))
    
    pygame.draw.rect(screen, tuple( 40 for x in range(0,3)), (screen_x*.06, screen_y*.34, screen_y*.12, screen_y*.12))
    screen.blit(pygame.transform.scale(pm_right[0], (screen_y*.1, screen_y*.1)), (screen_x*.068, screen_y*.352))
    screen.blit(pygame.transform.scale(gr_right[0], (screen_y*.12, screen_y*.12)), (screen_x*.06, screen_y*.50))
    pygame.draw.rect(screen, (80, 20, 250), (screen_x*.06, screen_y*.66, screen_y*.12, screen_y*.12))
    pygame.draw.rect(screen, tuple( 40 for x in range(0,3)), (screen_x*.06, screen_y*.82, screen_y*.12, screen_y*.12))
    pygame.draw.circle(screen, (231, 218, 109), (screen_x*.06+screen_y*.12/2, screen_y*.82+screen_y*.12/2), screen_y*.02)
    
    pygame.draw.rect(screen, tuple(40 for x in range(0,3)), (screen_x*.04, screen_y*.20, screen_x*.22, screen_y*.1))
    write("SAVE", screen_x*.1, screen_y*.216, "white", int(screen_y*.08))
    
    if mouse[0] and not mouse_save[0] and screen_x*.04<mouse_pos[0]<screen_x*.26 and screen_y*.2<mouse_pos[1]<screen_y*.3:
        grid_save_str = []
        for x in grid_save:
            grid_save_str.append("".join(x))
        grid_save_str = "\n".join(grid_save_str)
        
        current_time = datetime.now()
        current_time = str(current_time).replace(" ", "_").replace(":", ".")
        
        with open(f"pacman\\levels\\{current_time}.txt", "w", encoding = "UTF-8") as file:
            file.write(grid_save_str)
    
    colour_fix = lambda xory: "white" if xory == selected_coord[1] else tuple( 40 for x in range(0,3))
    write(f"x [{BLANK.join(write_xy['x'])}]", screen_x*.05, screen_y*.05//1, colour_fix("x"), int(screen_y*.05))
    write(f"y [{BLANK.join(write_xy['y'])}]", screen_x*.05, screen_y*.12//1, colour_fix("y"), int(screen_y*.05))
    
    pygame.display.update()
    clock.tick(60)
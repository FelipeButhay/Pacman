import os

pitagoras = lambda c1, c2: (c1**2 + c2**2)**0.5
direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')

def path_finder(pos, facing, grid):
    with open(f"{direc}\\lvl\\lvl.txt", "r", encoding = "UTF-8") as file:
        grid_str = file.read().split("\n")
    grid_save = []
    for x in grid_str:
        grid_save.append(",".join(x).split(","))
        
    for xx, x in enumerate(grid_save):
        for yy, y in enumerate(x):
            if y != "b" and y != "g":
                grid_save[xx][yy] = " "
                
    around = [(0,-1), (-1,0), (1,0), (0,1)]
    for yy, y in enumerate(grid_save):
        if "g" in y:
            target = [yy, y.index("g")]
            break
    
    grid_save[int(pos[0])][int(pos[1])] = "G"
    grid_save[int(target[0])][int(target[1])] = "T"

    n = 0
    inicial_p = [(int(target[0]), int(target[1]))]
    finding = True
    while finding:
        finding = False
        for x in grid_save:
            if " " in x:
                finding = True

        n += 1
        inicial_p_save = inicial_p[:]
        inicial_p.clear()
        for y in inicial_p_save:
            for x in around:
                if grid_save[(y[0]+x[0])%grid[0]][(y[1]+x[1])%grid[1]] == " ":
                    grid_save[(y[0]+x[0])%grid[0]][(y[1]+x[1])%grid[1]] = n
                    inicial_p.append(((y[0]+x[0])%grid[0], (y[1]+x[1])%grid[1]))
                if grid_save[(y[0]+x[0])%grid[0]][(y[1]+x[1])%grid[1]] == "G":
                    finding = False
    grid_save[int(target[0])][int(target[1])] = 0
    
    around_ns = []         
    for x in around[:]:
        if type(grid_save[int(pos[0])+x[0]][int(pos[1])+x[1]]) == type(0):
            around_ns.append(grid_save[int(pos[0])+x[0]][int(pos[1])+x[1]])
        else:
            around.remove(x)
        
    return around[around_ns.index(min(around_ns))], min(around_ns)
    
def behaviour(facing, pos, pacman, ghosts, blocks, grid_save, colour, eatable, dead):
    # for x in ghosts[:]:
    #     if x.pos == [-10, -10]:
    #         ghosts.remove(x)
    
    around = [(0,-1), (-1,0), (1,0), (0,1)]
    around_pit = []
    around.remove((-facing[0], -facing[1]))
    for x in around[:]:
        if (int(pos[0])+x[0], int(pos[1])+x[1]) in blocks:
            around.remove(x)   
            
    if eatable:
        for x in around:
            target = pacman.pos
            around_pit.append(pitagoras(pos[0]-target[0]+x[0], pos[1]-target[1]+x[1]))
        try:
            return around[around_pit.index(max(around_pit))]
        except:
            return facing
        
    match colour:
        case 0:
            for x in around:
                target = pacman.pos
                around_pit.append(pitagoras(pos[0]-target[0]+x[0], pos[1]-target[1]+x[1]))
            try:
                return around[around_pit.index(min(around_pit))]
            except:
                return facing
        case 1:
            for x in around:
                target = (pacman.pos[0]+3*pacman.facing[0], pacman.pos[1]+3*pacman.facing[1])
                around_pit.append(pitagoras(pos[0]-target[0]+x[0], pos[1]-target[1]+x[1]))
            try:
                return around[around_pit.index(min(around_pit))]
            except:
                return facing
        case 2:
            for x in around:
                for y in ghosts:
                    if y.colour == 0:
                        red = y.pos
                target = (pacman.pos[0]-red[0], pacman.pos[1]-red[1])
                around_pit.append(pitagoras(pos[0]-target[0]+x[0], pos[1]-target[1]+x[1]))
            try:
                return around[around_pit.index(min(around_pit))]
            except:
                return facing
        case 3:
            for x in around:
                if pitagoras(pos[0]-pacman.pos[0], pos[1]-pacman.pos[1]) > 6.5:
                    target = pacman.pos
                else:
                    target = (-1, -1)
                around_pit.append(pitagoras(pos[0]-target[0]+x[0], pos[1]-target[1]+x[1]))
            try:
                return around[around_pit.index(min(around_pit))]
            except:
                return facing
import random
#Generate Random Map
def generate_random_map_custom(size:int, ratio:float):
    grid = [['F'] * size for _ in range(size)]
    n_holes = int(size * size * ratio)
    grid_states = [[j * size + i for i in range(size)] for j in range(size)]
    
    state0 = state1 = 0

    for i in range(n_holes):
        pos_x = random.randint(0,size-1)
        pos_y = random.randint(0,size-1)
        grid[pos_y][pos_x] = 'H'

    while True:
        pos_x = random.randint(0,size-1)
        pos_y = random.randint(0,size-1)
        if grid[pos_y][pos_x] == 'F':
            grid[pos_y][pos_x] = 'S'
            state0 = (pos_y,pos_x,0)
            break    

    while True:
        pos_x = random.randint(0,size-1)
        pos_y = random.randint(0,size-1)
        if grid[pos_y][pos_x] == 'F':
            grid[pos_y][pos_x] = 'G'
            #state1 = grid_states[pos_y][pos_x]
            state1 = (pos_y,pos_x)
            break

    grid = [''.join(row) for row in grid]

    return grid , state0 , state1

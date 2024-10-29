from collections import deque
import time

# Función para verificar si la posición está dentro de los límites y no es un agujero
def is_valid(x, y, lake, visited):
    rows, cols = len(lake), len(lake[0])
    return 0 <= x < rows and 0 <= y < cols and lake[x][y] != 'H' and (x, y) not in visited

# BFS
def bfs_frozenlake(lake,directions,start):
    #Inicializamos el Tiempo
    start_time = time.time()
    #Inicializamos Costo
    cost_1 = 0
    cost_2 = 0
    states = 0
    
    if not start:
        return None  # Si no se encuentra el estado inicial

    queue = deque([(start, [])]) 
    visited = set([start])

    while queue:
        (x, y , cost_0), path = queue.popleft()
        states += 1
        #print(cost)

        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos
                cost_1 += 1
                cost_2 += move[2]

            #Finalizamos el tiempo
            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], states, elapsed_time, cost_1, cost_2)

        # Probar todas las direcciones posibles
        for direction in directions:
            new_x, new_y , cost_0 = x + direction[0], y + direction[1], direction[2]
            if is_valid(new_x, new_y, lake, visited):
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y, cost_0), path + [direction]))
    
    end_time = time.time()

    elapsed_time = end_time - start_time

    return ([], states,elapsed_time,cost_1,cost_2)  

# DFS
def dfs_frozenlake(lake, directions, start):
    start_time = time.time()

    stack = [(start, [])]
    visited = set([start])

    states = 0
    cost_1 = 0
    cost_2 = 0
    costo_total = 0

    while stack:
        (x, y, cost_0), path = stack.pop()
        costo_total += cost_0
        states += 1

        
        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos
                cost_1 += 1
                cost_2 += move[2]

            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], states, cost_1, cost_2, elapsed_time)

        # Probar todas las direcciones posibles
        for direction in directions:
            new_x, new_y , new_cost = x + direction[0], y + direction[1], direction[2]
            if is_valid(new_x, new_y, lake, visited):
                visited.add((new_x, new_y))
                stack.append(((new_x, new_y, new_cost), path + [direction]))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return ([], states, cost_1, cost_2, elapsed_time) 

# DFS con límite de profundidad
def depth_limited_search(lake, directions, limit, start):
    stack = [(start, [], 0)]  # Pila con (posición actual, camino de movimientos, profundidad)
    visited = set([start])

    states = 0
    cost_1 = 0 
    cost_2 = 0
    start_time = time.time()

    while stack:
        k = stack.pop()
        (x, y , cost_0), path, depth = k

        states += 1
        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos
                cost_1 += 1
                cost_2 += move[2]

            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], states, cost_1, cost_2, elapsed_time)

        # Limitar la profundidad
        if depth < limit:
            # Probar todas las direcciones posibles
            for direction in directions:
                new_x, new_y , new_cost = x + direction[0], y + direction[1] , direction[2]

                if is_valid(new_x, new_y, lake, visited):
                    visited.add((new_x, new_y))
                    stack.append(((new_x, new_y, new_cost), path + [direction], depth + 1))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return  ([], states, cost_1, cost_2, elapsed_time)
    

from heapq import heappush, heappop

# UCS 
def uniform_cost_search_with_variable_cost(lake, directions, start):
    start_time = time.time()
    
    priority_queue = [(0, start, [])]  # Cola de prioridad con (costo acumulado, posición actual, camino de movimientos)
    visited = set()

    states = 0
    cost_1 = 0 
    cost_2 = 0

    while priority_queue:
        cost, (x, y), path = heappop(priority_queue)
        states += 1

        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos
                cost_1 += 1
                cost_2 += move[2]

            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], states, cost_1, cost_2, elapsed_time)

        if (x, y) not in visited:
            visited.add((x, y))
            # Probar todas las direcciones posibles con su costo
            for direction in directions:
                new_x, new_y, move_cost = x + direction[0], y + direction[1], direction[2]
                new_total_cost = cost + move_cost  # Acumulamos el costo

                if is_valid(new_x, new_y, lake, visited):
                    heappush(priority_queue, (new_total_cost, (new_x, new_y), path + [direction]))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return ([], elapsed_time, 0) 


import random

# Función para moverse aleatoriamente hasta encontrar la meta o fallar
def random_search(lake, directions, start, max_moves=100):
    # Estado inicial
    x, y = start
    path = [(lake[x][y], (x, y))]
    
    start_time = time.time()
    states = 0
    cost_1 = 0
    cost_2 = 0

    for _ in range(max_moves):
        states += 1

        if lake[x][y] == 'G':
            end_time = time.time()
            elapsed_time = end_time - start_time
            return (path + [(lake[x][y], (x, y))], states, cost_1, cost_2, elapsed_time)
        
        # Escoger un movimiento aleatorio
        direction = random.choice(directions)
        new_x, new_y, new_cost = x + direction[0], y + direction[1], direction[2]

        cost_1 += 1
        cost_2 += new_cost

        if is_valid(new_x, new_y, lake, set()):
            x, y = new_x, new_y
            path.append((lake[x][y], (x, y)))
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return ([], states, cost_1, cost_2, elapsed_time)  # Si no se encuentra la meta en el número máximo de movimientos



from heapq import heappush, heappop

# Heuristica
def manhattan_distance(x, y, goal_x, goal_y):
    return abs(x - goal_x) + abs(y - goal_y)

# A* para encontrar el camino más corto
def a_star_search(lake, start, goal, directions):

    priority_queue = [(0, 0, start, [])]  
    visited = set()
    goal_x, goal_y = goal
    states = 0
    cost_1 = 0 
    while priority_queue:
        k = heappop(priority_queue)
        #print(k)
        _, real_cost, (x, y, z), path = k

        start_time = time.time()

        if lake[x][y] == 'G':
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos

                cost_1 += 1
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], states, cost_1, real_cost, elapsed_time)

        if (x, y) not in visited:
            visited.add((x, y))
            states += 1
            # Probar todas las direcciones posibles
            for direction in directions:
                new_x, new_y, move_cost = x + direction[0], y + direction[1], direction[2]
                
                if is_valid(new_x, new_y, lake, visited):
                    # Costo acumulado real y heurístico (distancia Manhattan)
                    new_real_cost = real_cost + move_cost
                    heuristic = manhattan_distance(new_x, new_y, goal_x, goal_y)
                    total_cost = new_real_cost + heuristic  # f(n) = g(n) + h(n)
                    heappush(priority_queue, (total_cost, new_real_cost, (new_x, new_y, move_cost), path + [direction]))
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return ([], states, 0, 0, elapsed_time)
from collections import deque
import time



# Función para verificar si la posición está dentro de los límites y no es un agujero
def is_valid(x, y, lake, visited):
    rows, cols = len(lake), len(lake[0])
    return 0 <= x < rows and 0 <= y < cols and lake[x][y] != 'H' and (x, y) not in visited

# BFS para encontrar el camino más corto
def bfs_frozenlake(lake,directions,start):
    #Inicializamos el Tiempo
    start_time = time.time()
    #Inicializamos Costo
    cost = 0
    states = 0
    
    if not start:
        return None  # Si no se encuentra el estado inicial

    queue = deque([(start, [])])  # (posición actual, camino de movimientos)
    visited = set([start])

    while queue:
        (x, y , cost_0), path = queue.popleft()
        cost += cost_0
        states += 1
        #print(cost)
        # Si llegamos a la meta 'G', devolvemos el camino
        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos

            #Finalizamos el tiempo
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Estados Explorados",states)
            return (result_path + [(lake[x][y], (x, y))], elapsed_time, cost)

        # Probar todas las direcciones posibles
        for direction in directions:
            new_x, new_y , cost_0 = x + direction[0], y + direction[1], direction[2]
            if is_valid(new_x, new_y, lake, visited):
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y, cost_0), path + [direction]))
    
    #Finalizamos el tiempo
    end_time = time.time()

    elapsed_time = end_time - start_time

    return ([],elapsed_time,cost)  # Si no se encuentra solución


# DFS para encontrar el camino más corto
def dfs_frozenlake(lake, directions, start):
    start_time = time.time()

    stack = [(start, [])]  # Pila con (posición actual, camino de movimientos)
    visited = set([start])
    costo_total = 0

    while stack:
        (x, y, cost_0), path = stack.pop()
        costo_total += cost_0

        # Si llegamos a la meta 'G', devolvemos el camino
        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos

            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], elapsed_time , costo_total)

        # Probar todas las direcciones posibles
        for direction in directions:
            new_x, new_y , new_cost = x + direction[0], y + direction[1], direction[2]
            if is_valid(new_x, new_y, lake, visited):
                visited.add((new_x, new_y))
                stack.append(((new_x, new_y, new_cost), path + [direction]))

    end_time = time.time()
    elapsed_time = end_time - start_time
    return ([],costo_total,elapsed_time)  # Si no se encuentra solución


from heapq import heappush, heappop

# UCS para encontrar el camino con el menor costo variable
def uniform_cost_search_with_variable_cost(lake, directions, start):
    start_time = time.time()
    
    priority_queue = [(0, start, [])]  # Cola de prioridad con (costo acumulado, posición actual, camino de movimientos)
    visited = set()

    while priority_queue:
        cost, (x, y), path = heappop(priority_queue)

        # Si llegamos a la meta 'G', devolvemos el camino
        if lake[x][y] == 'G':
            # Convertir el camino de movimientos a posiciones y nombres de movimientos
            result_path = []
            curr_pos = start
            for move in path:
                next_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
                result_path.append((lake[next_pos[0]][next_pos[1]], next_pos))
                curr_pos = next_pos

            end_time = time.time()
            elapsed_time = end_time - start_time
            return (result_path + [(lake[x][y], (x, y))], elapsed_time, cost)

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
    return ([], elapsed_time, 0)  # Si no se encuentra solución




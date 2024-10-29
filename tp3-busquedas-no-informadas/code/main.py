from collections import deque
import time
import pandas as pd
import map

from search_algorithms import bfs_frozenlake, dfs_frozenlake , uniform_cost_search_with_variable_cost, depth_limited_search,random_search,a_star_search


# Lista para almacenar los resultados
results = []
# Direcciones
directions_1 = [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1)]  # Arriba, Abajo, Izquierda, Derecha , Costo
directions_2 = [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]  # Arriba, Abajo, Izquierda, Derecha , Costo
direction_names = ["Arriba", "Abajo", "Izquierda", "Derecha"]

for i in range(30):
    mapa ,state_0 , state_1= map.generate_random_map_custom(100,0.08)
    x , y , z = state_0
    #BFS
    (path, states, time_path , cost_1 , cost_2)  = bfs_frozenlake(mapa,directions_2,state_0)
    #print(path)
    results.append({
        'Algorithm': 'BFS',
        'evn_n': i,
        'states': states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })

    #DFS
    (path, states, cost_1, cost_2, time_path)  = dfs_frozenlake(mapa, directions_2, state_0)
    results.append({
        'Algorithm': 'DFS',
        'evn_n': i,
        'states' : states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })

    #DFS Limite 10
    (path, states, cost_1, cost_2, time_path)  = depth_limited_search(mapa, directions_2, 10, state_0)
    results.append({
        'Algorithm': 'DFS Limit 10',
        'evn_n': i,
        'states' : states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })

    #UFC
    (path, states, cost_1, cost_2, time_path)  = uniform_cost_search_with_variable_cost(mapa,directions_2,(x,y))
    results.append({
        'Algorithm': 'UCS',
        'evn_n': i,
        'states' : states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })
    
    #Aleatorio

    (path, states, cost_1, cost_2, time_path)  = random_search(mapa,directions_2,(x,y),1000)
    results.append({
        'Algorithm': 'Random Walk',
        'evn_n': i,
        'states' : states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })

    #A*

    (path, states, cost_1, cost_2, time_path)  = a_star_search(mapa, state_0, state_1, directions_2)
    results.append({
        'Algorithm': 'A*',
        'evn_n': i,
        'states' : states,
        'cost_e1': cost_1,
        'cost_e2': cost_2,
        'time': time_path,
        'solution_found' : len(path) > 0
    })
    

df = pd.DataFrame(results)
print(df)

df.to_csv('search_results.csv', index=False)
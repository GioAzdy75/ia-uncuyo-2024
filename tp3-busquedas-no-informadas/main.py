import gymnasium as gym
from collections import deque
import map
import time
import pandas as pd

from tp3.search_algorithms import bfs_frozenlake, dfs_frozenlake , uniform_cost_search_with_variable_cost


# Lista para almacenar los resultados
results = []
# Direcciones
directions_1 = [(-1, 0, 1), (1, 0, 1), (0, -1, 1), (0, 1, 1)]  # Arriba, Abajo, Izquierda, Derecha , Costo
directions_2 = [(-1, 0, 1), (1, 0, 2), (0, -1, 3), (0, 1, 4)]  # Arriba, Abajo, Izquierda, Derecha , Costo
direction_names = ["Arriba", "Abajo", "Izquierda", "Derecha"]

for i in range(5):
    mapa ,state_0 , state_1= map.generate_random_map_custom(100,0.08)

    x , y , z = state_0
    
    #BFS
    (path, time_path , cost)  = bfs_frozenlake(mapa,directions_1,state_0)

    print(path)
    results.append({
        'Algorithm': 'BFS Frozen Lake',
        'evn_n': len(path),
        'cost_e1': cost,
        'cost_e2': cost,
        'time': time_path,
        'solution_found' : len(path) > 0
    })
    #DFS
    (path, time_path , cost)  = dfs_frozenlake(mapa,directions_1,state_0)
    results.append({
        'Algorithm': 'DFS Frozen Lake',
        'evn_n': len(path),
        'cost_e1': cost,
        'cost_e2': cost,
        'time': time_path,
        'solution_found' : len(path) > 0
    })
    #DFS Limite 10


    #UFC
    (path, time_path , cost)  = uniform_cost_search_with_variable_cost(mapa,directions_2,(x,y))
    results.append({
        'Algorithm': 'Uniform Cost with Variable Cost',
        'evn_n': len(path),
        'cost_e1': cost,
        'cost_e2': cost,
        'time': time_path,
        'solution_found' : len(path) > 0
    })
    
    #Aleatorio


# Crear un DataFrame a partir de los resultados
df = pd.DataFrame(results)
print(df)

# Exportar el DataFrame a un archivo CSV
#df.to_csv('search_results.csv', index=False)

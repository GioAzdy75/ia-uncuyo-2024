import numpy as np
import time

def count_attacking_pairs(board):
    """Contabiliza el número de pares de reinas atacándose mutuamente."""
    N = len(board)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

def generate_neighbor(board):
    """Genera un vecino del tablero actual cambiando la fila de una reina."""
    N = len(board)
    neighbor = board.copy()
    row = np.random.randint(N)
    col = np.random.randint(N)
    while neighbor[row] == col:
        col = np.random.randint(N)
    neighbor[row] = col
    return neighbor

def hill_climbing(N, max_states):
    """Algoritmo de Hill Climbing para resolver el problema de las N-reinas."""
    start_time = time.time()
    current = np.random.randint(N, size=N)
    current_cost = count_attacking_pairs(current)
    states_evaluated = 0
    
    while states_evaluated < max_states:
        neighbor = generate_neighbor(current)
        neighbor_cost = count_attacking_pairs(neighbor)
        states_evaluated += 1
        
        if neighbor_cost < current_cost:
            current = neighbor
            current_cost = neighbor_cost
            
        if current_cost == 0:
            break
    
    end_time = time.time()
    return current, current_cost, states_evaluated, end_time - start_time


def simulated_annealing(N, max_states, initial_temp, cooling_rate):
    """Algoritmo Simulated Annealing para resolver el problema de las N-reinas."""
    def temperature(t, cooling_rate):
        return initial_temp * (cooling_rate ** t)
    
    start_time = time.time()
    current = np.random.randint(N, size=N)
    current_cost = count_attacking_pairs(current)
    states_evaluated = 0
    t = 0
    
    while states_evaluated < max_states:
        neighbor = generate_neighbor(current)
        neighbor_cost = count_attacking_pairs(neighbor)
        delta_cost = neighbor_cost - current_cost
        
        if delta_cost < 0 or np.random.rand() < np.exp(-delta_cost / temperature(t, cooling_rate)):
            current = neighbor
            current_cost = neighbor_cost
        
        states_evaluated += 1
        t += 1
        
        if current_cost == 0:
            break
    
    end_time = time.time()
    return current, current_cost, states_evaluated, end_time - start_time

def crossover(parent1, parent2):
    """Cruza dos padres para crear un nuevo hijo."""
    N = len(parent1)
    point = np.random.randint(1, N)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return child1, child2

def mutate(board, mutation_rate):
    """Aplica mutación al tablero con una cierta tasa de mutación."""
    N = len(board)
    mutated = board.copy()
    for i in range(N):
        if np.random.rand() < mutation_rate:
            mutated[i] = np.random.randint(N)
    return mutated

def genetic_algorithm(N, max_generations, population_size, mutation_rate):
    """Algoritmo Genético para resolver el problema de las N-reinas."""
    start_time = time.time()
    population = [np.random.randint(N, size=N) for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')
    generations = 0
    
    while generations < max_generations:
        population = sorted(population, key=lambda x: count_attacking_pairs(x))
        current_best = population[0]
        current_best_cost = count_attacking_pairs(current_best)
        
        if current_best_cost < best_cost:
            best_cost = current_best_cost
            best_solution = current_best
        
        if best_cost == 0:
            break
        
        new_population = population[:2]  # Keep the best two

        while len(new_population) < population_size:
            parents = np.array(population[:10])
            parent_indices = np.random.choice(len(parents), 2, replace=False)
            parent1, parent2 = parents[parent_indices[0]], parents[parent_indices[1]]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        
        population = new_population
        generations += 1
    
    end_time = time.time()
    return best_solution, best_cost, generations, end_time - start_time


import pandas as pd

def run_experiments():
    N_values = [4, 8, 10]
    algorithms = {
        'Hill Climbing': hill_climbing,
        'Simulated Annealing': simulated_annealing,
        'Genetic Algorithm': genetic_algorithm
    }
    
    results = []
    
    for N in N_values:
        for name, algo in algorithms.items():
            for i in range(30):
                if name == 'Hill Climbing':
                    solution, cost, states, time_elapsed = algo(N, 10000)
                elif name == 'Simulated Annealing':
                    solution, cost, states, time_elapsed = algo(N, 10000, 10000, 0.995)
                elif name == 'Genetic Algorithm':
                    solution, cost, generations, time_elapsed = algo(N, 1000, 50, 0.1)
                    states = generations
                
                results.append({
                    'Algorithm': name,
                    'N': N,
                    'Solution Cost': cost,
                    'States/Generations': states,
                    'Time': time_elapsed
                })
    
    df = pd.DataFrame(results)
    print(df)
    df.to_csv('tp5-Nreinas.csv', index=False)

run_experiments()

#Backtracking
def es_seguro(tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i] == columna:
            return  
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True

def resolver_reinas_backtracking(tablero, fila, n, soluciones, estados):
    if fila == n:
        soluciones.append(tablero[:])
        return
    for columna in range(n):
        estados[0] += 1
        if es_seguro(tablero, fila, columna, n):
            tablero[fila] = columna
            resolver_reinas_backtracking(tablero, fila + 1, n, soluciones, estados)

def n_reinas_backtracking(n):
    tablero = [-1] * n
    soluciones = []
    estados = [0]
    resolver_reinas_backtracking(tablero, 0, n, soluciones, estados)
    return soluciones, estados[0]

#Forward
def forward_checking(tablero, dominios, fila, columna, n):
    # Actualiza los dominios al colocar una reina en fila y columna
    for i in range(fila + 1, n): 
        if columna in dominios[i]:
            dominios[i].remove(columna)

        diag_izq = columna - (i - fila)
        diag_der = columna + (i - fila)
        if diag_izq in dominios[i]:
            dominios[i].remove(diag_izq)
        if diag_der in dominios[i]:
            dominios[i].remove(diag_der)
    return dominios

def resolver_reinas_forward(tablero, dominios, fila, n, soluciones, estados):
    estados[0] += 1  # Contamos cada estado explorado
    if fila == n:
        soluciones.append(tablero[:])
        return
    columnas = dominios[fila][:]
    for columna in columnas:
        nuevo_dominio = [dom[:] for dom in dominios]
        tablero[fila] = columna
        # Actualizamos los dominios según forward checking
        nuevo_dominio = forward_checking(tablero, nuevo_dominio, fila, columna, n)
        resolver_reinas_forward(tablero, nuevo_dominio, fila + 1, n, soluciones, estados)

def n_reinas_forward(n):
    tablero = [-1] * n
    dominios = [list(range(n)) for _ in range(n)]
    soluciones = []
    estados = [0]  # Lista para contar lo estados
    resolver_reinas_forward(tablero, dominios, 0, n, soluciones, estados)
    return soluciones, estados[0]


import time
import csv

def ejecutar_algoritmos(n, num_iteraciones):
    resultados = []
    for i in range(num_iteraciones):
        # Backtracking
        inicio = time.time()
        soluciones_backtracking, estados_backtracking = n_reinas_backtracking(n)
        tiempo_backtracking = time.time() - inicio

        # Forward Checking
        inicio = time.time()
        soluciones_forward, estados_forward = n_reinas_forward(n)
        tiempo_forward = time.time() - inicio

        resultados.append([n, tiempo_backtracking, len(soluciones_backtracking), estados_backtracking, 
                           tiempo_forward, len(soluciones_forward), estados_forward])

    return resultados

def guardar_csv(resultados, archivo_csv):
    with open(archivo_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["N", "Tiempo Backtracking", "Soluciones Backtracking", "Estados Backtracking", 
                         "Tiempo Forward", "Soluciones Forward", "Estados Forward"])
        writer.writerows(resultados)

resultados_4 = ejecutar_algoritmos(4, 30)
resultados_8 = ejecutar_algoritmos(8, 30)
resultados_10 = ejecutar_algoritmos(10, 30)

guardar_csv(resultados_4 + resultados_8 + resultados_10, 'tp6-Nreinas.csv')

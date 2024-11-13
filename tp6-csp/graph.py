import pandas as pd
import matplotlib.pyplot as plt


#Main
df = pd.read_csv("tp6-Nreinas.csv")
print(df)

import pandas as pd
import matplotlib.pyplot as plt

# Supongamos que df es el DataFrame que has proporcionado.

# Filtrar los tamaños 4, 8 y 10
df_filtrado = df[df['N'].isin([4, 8, 10])]

# Seleccionar las columnas necesarias para los estados explorados
df_filtrado = df_filtrado[['N', 'Estados Backtracking', 'Estados Forward']]

# Agrupar por el tamaño (N) y sumar los estados explorados
df_agrupado = df_filtrado.groupby('N').agg({
    'Estados Backtracking': 'mean',  # Promedio de los estados explorados con Backtracking
    'Estados Forward': 'mean'        # Promedio de los estados explorados con Forward
}).reset_index()

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))

# Definir el ancho de las barras
bar_width = 0.35

# Crear las barras para Backtracking y Forward
plt.bar(df_agrupado['N'] - bar_width/2, df_agrupado['Estados Backtracking'], bar_width, label='Backtracking', color='b')
plt.bar(df_agrupado['N'] + bar_width/2, df_agrupado['Estados Forward'], bar_width, label='Forward', color='g')

# Agregar etiquetas y título
plt.xlabel('Tamaño (N)', fontsize=12)
plt.ylabel('Estados Explorados', fontsize=12)
plt.title('Comparación de Estados Explorados: Backtracking vs Forward', fontsize=14)
plt.xticks(df_agrupado['N'])  # Para mostrar solo los valores de N: 4, 8, 10
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Supongamos que df es el DataFrame que has proporcionado.

# Filtrar los tamaños 4, 8 y 10
df_filtrado = df[df['N'].isin([4, 8, 10])]

# Seleccionar las columnas necesarias para el tiempo
df_filtrado = df_filtrado[['N', 'Tiempo Backtracking', 'Tiempo Forward']]

# Agrupar por el tamaño (N) y calcular el promedio del tiempo
df_agrupado = df_filtrado.groupby('N').agg({
    'Tiempo Backtracking': 'mean',  # Promedio de tiempo de Backtracking
    'Tiempo Forward': 'mean'        # Promedio de tiempo de Forward
}).reset_index()

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))

# Definir el ancho de las barras
bar_width = 0.35

# Crear las barras para Backtracking y Forward
plt.bar(df_agrupado['N'] - bar_width/2, df_agrupado['Tiempo Backtracking'], bar_width, label='Backtracking', color='b')
plt.bar(df_agrupado['N'] + bar_width/2, df_agrupado['Tiempo Forward'], bar_width, label='Forward', color='g')

# Agregar etiquetas y título
plt.xlabel('Tamaño (N)', fontsize=12)
plt.ylabel('Tiempo (segundos)', fontsize=12)
plt.title('Comparación de Tiempo de Ejecución: Backtracking vs Forward', fontsize=14)
plt.xticks(df_agrupado['N'])  # Para mostrar solo los valores de N: 4, 8, 10
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()

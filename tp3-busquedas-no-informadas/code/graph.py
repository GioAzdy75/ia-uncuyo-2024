import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('search_results.csv')

df = df[df['solution_found'] == True]

#Grafo 1

plt.figure(figsize=(12, 6))
sns.boxplot(x='Algorithm', y='states', data=df)

plt.xticks(rotation=45)
plt.title('Comparación de Estados por Algoritmo')
plt.xlabel('Algoritmo')
plt.ylabel('Número de Estados')
plt.grid(True)
plt.tight_layout()

plt.show()

# Grafo 2
plt.figure(figsize=(12, 6))
sns.boxplot(x='Algorithm', y='time', data=df)

plt.xticks(rotation=45)
plt.title('Comparación de Tiempo por Algoritmo')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (s)')
plt.grid(True)
plt.tight_layout()

plt.show()

# Grafo 3
plt.figure(figsize=(12, 6))
sns.boxplot(x='Algorithm', y='cost_e1', data=df)

plt.xticks(rotation=45)
plt.title('Comparación de Costos e_1 por Algoritmo')
plt.xlabel('Algoritmo')
plt.ylabel('Costo e_1')
plt.grid(True)
plt.tight_layout()

plt.show()

# Grafo 4
plt.figure(figsize=(12, 6))
sns.boxplot(x='Algorithm', y='cost_e2', data=df)

plt.xticks(rotation=45)
plt.title('Comparación de Costos e_2 por Algoritmo')
plt.xlabel('Algoritmo')
plt.ylabel('Costo e_2')
plt.grid(True)
plt.tight_layout()

plt.show()
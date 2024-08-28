import pandas as pd
import matplotlib as plt
from matplotlib import pyplot as plt
from matplotlib import colors


def export_dataframes(name:str,df):
    # Exportar el DataFrame Original a formato Markdown
    file_path = f'C:/Users/yugii/Desktop/{name}.md'
    markdown_table = df.to_markdown(index=False)
    # Guardar en un archivo .md
    with open(file_path, 'w') as file:
        file.write(markdown_table)

df1 = pd.read_csv('ReflexiveAgentData.csv')
df2 = pd.read_csv('RandomAgentData.csv')

def promedios(df):
    # Agrupar por el nombre del agente y calcular el promedio de Valor1 y Valor2
    promedios = df.groupby(['Agente','Suciedad']).agg({'Movimientos': 'mean', 'Performance': 'mean'}).reset_index()
    # Renombrar columnas para claridad
    promedios.rename(columns={'Movimientos': 'Promedio Movimientos', 'Performance': 'Promedio Performance'}, inplace=True)
    # Mostrar el DataFrame con los promedios
    return promedios

#Promedios df
df1promedios = promedios(df1)
df2promedios = promedios(df2)

print(df1promedios)
print('#####')
print(df2promedios)


def plotGraph(name,df):
    plt.figure(figsize=(10, 6))
    for suciedad in df['Suciedad'].unique():
        subset = df[df['Suciedad'] == suciedad]
        plt.scatter(subset['Promedio Performance'], subset['Promedio Movimientos'], label=f'Suciedad {suciedad}')
    # Añadir etiquetas y título
    plt.xlabel('Promedio Performance')
    plt.ylabel('Promedio Movimientos')
    plt.title(f'Scatter Plot {name}')
    plt.legend(title='Suciedad')
    plt.grid(True)
    # Mostrar el plot
    plt.show()

#plotGraph('Agente Reflexivo',df1promedios)
#plotGraph('Agente Aleatorio',df2promedios)
import math
z = [128,16,2,32,4,64,8]
total_basura = []
while len(z) != 0:
    x = z.pop(0)
    total_basura += [math.ceil(x*x*0.1),math.ceil(x*x*0.2),math.ceil(x*x*0.4),math.ceil(x*x*0.8)]

df2promedios['Total Suciedad'] = total_basura
df2promedios['Porcentaje Suciedad Limpiada'] = (df2promedios['Promedio Performance'] * 100) / df2promedios['Total Suciedad']
print(df2promedios)

#
df1_filtrado = df1promedios.loc[df1promedios['Suciedad'] == 0.1]
df2_filtrado = df2promedios.loc[df2promedios['Suciedad'] == 0.1]
# Niveles de suciedad
niveles_suciedad = [0.1, 0.2, 0.4, 0.8]

agent_labels = ['Agente 2x2' , 'Agente 4x4' , 'Agente 8x8' , 'Agente 16x16' , 'Agente 32x32' , 'Agente 64x64', 'Agente 128x128']




import numpy as np


def grafico1(df1,df2,suciedad):
    #Filtramos los DataFrames
    df1_filtrado = df1.loc[df1['Suciedad'] == suciedad]
    df2_filtrado = df2.loc[df2['Suciedad'] == suciedad]

    # Asegúrate de que ambos DataFrames tienen las mismas etiquetas de agentes
    df1_filtrado = df1_filtrado.set_index('Agente').reindex(agent_labels).reset_index()
    df2_filtrado = df2_filtrado.set_index('Agente').reindex(agent_labels).reset_index()

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(12, 8))

    # Ancho de las barras
    bar_width = 0.35

    # Posiciones de las barras en el eje X
    index = np.arange(len(agent_labels))

    # Crear barras para df1
    bars1 = ax.bar(index - bar_width / 2, df1_filtrado['Promedio Performance'], bar_width, label='Agente Reflexivo')

    # Crear barras para df2
    bars2 = ax.bar(index + bar_width / 2, df2_filtrado['Promedio Performance'], bar_width, label='Agente Random')

    # Configurar etiquetas y título
    ax.set_xlabel('Agente')
    ax.set_ylabel('Promedio Performance')
    ax.set_title(f'Comparación de Promedio Performance entre Agentes con suciedad al {suciedad}')
    ax.set_xticks(index)
    ax.set_xticklabels(agent_labels, rotation=45, ha='right')
    ax.legend()

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


#grafico1(df1promedios,df2promedios,0.1)
#grafico1(df1promedios,df2promedios,0.2)
#grafico1(df1promedios,df2promedios,0.4)
#grafico1(df1promedios,df2promedios,0.8)

print('Fin Programa')

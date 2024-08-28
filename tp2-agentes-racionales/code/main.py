from environment import Environment
from agent import RandomAgent,Agent,ReflexiveAgent
import random

from matplotlib import pyplot as plt
from matplotlib import colors

import pandas as pd
import numpy as np

import copy

#Guardar Mapas
def saveMap(name,env:Environment):
    cmap = colors.ListedColormap(['white','red'])
    plt.figure(figsize=(10,10))
    plt.pcolor(env.grid[::-1],cmap=cmap,edgecolors='k', linewidths=3)
    plt.savefig(f'maps/{name}.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

#Verifica si el entorno esta limpio
def check_entorno(env:Environment):
    return all(all(elemento == 0 for elemento in fila) for fila in env.grid)

#Ejecucion del Agente
def executeAgent(agent:Agent , env:Environment , name , iteracion):
    #for _ in range(1000):
    life = agent.life

    #saveMap(name + '-Inicio-' + f'{iteracion}',env)
    while agent.life > 0:
        if check_entorno(env):
            break
        agent.think()
    #saveMap(name + '-Final-' + f'{iteracion}',env)
    return [life - agent.life,agent.get_performance()]

def excuteAgents():
    '''Ejecuta un agente reflexivo y uno random con una serie de mapas preestablecidos'''

    x = ['Agente 2x2' , 'Agente 4x4' , 'Agente 8x8' , 'Agente 16x16' , 'Agente 32x32' , 'Agente 64x64', 'Agente 128x128']
    j = 0
    datos_reflexive = {'Agente 2x2' : [] , 'Agente 4x4' : [] , 'Agente 8x8' : [] , 'Agente 16x16' : [], 'Agente 32x32': [] , 
             'Agente 64x64': [], 'Agente 128x128' : []}
    
    datos_random = {'Agente 2x2' : [] , 'Agente 4x4' : [] , 'Agente 8x8' : [] , 'Agente 16x16' : [], 'Agente 32x32': [] , 
             'Agente 64x64': [], 'Agente 128x128' : []}
    cantidad_entornos = 7
    dirt_rates = [0.1,0.2,0.4,0.8]
    tamano = 2
    for i in range(cantidad_entornos):
        for k in range(len(dirt_rates)):
            for j in range(10):
                ejex = random.randint(0,tamano-1)
                ejey = random.randint(0,tamano-1)
                env = Environment(tamano,tamano,ejex,ejey,dirt_rates[k])
                env2 = copy.deepcopy(env)

                #Imprimir Mapa original 0.8
                if(tamano == 32 and j == 7):
                    saveMap('Original-32x32-Inicio-',env)
                #Reflexive
                agent = ReflexiveAgent(env)
                result = executeAgent(agent,agent.env,'Reflexivo ' + x[i],j)
                result.append(dirt_rates[k])
                datos_reflexive[x[i]].append(result)

                #Random
                agent = RandomAgent(env2)
                result = executeAgent(agent,agent.env,'Aleatorio ' +x[i],j)
                result.append(dirt_rates[k])
                datos_random[x[i]].append(result)

                #Imprimir Mapas Ejecutados
                if(tamano == 32 and j == 7):
                    saveMap('Reflexive-32x32-Final-',env)
                    saveMap('Random-32x32-Final-',env2)
        tamano *= 2
    return [datos_reflexive,datos_random]

def convertirDfs(data:dict):
    '''Convertimos los diccionarios en DataFrames'''
    # Lista para almacenar los DataFrames de cada agente
    dfs = []
    # Iterar sobre el diccionario para crear un DataFrame por cada tipo de agente
    for agente, valores in data.items():
        if valores:  # Verificar si la lista de valores no está vacía
            df = pd.DataFrame(valores, columns=['Movimientos', 'Performance', 'Suciedad'])
            df['Agente'] = agente  # Agregar una columna con el nombre del agente
            dfs.append(df)
    # Concatenar todos los DataFrames en uno solo
    df_final = pd.concat(dfs, ignore_index=True)
    return df_final


def export_dataframes(name:str,df):
    '''Exporta los datos de un Data Frame a csv'''
    # Exportar el DataFrame Original a formato Markdown
    file_path = f'C:/Users/yugii/Desktop/{name}.md'
    markdown_table = df.to_markdown(index=False)
    # Guardar en un archivo .md
    with open(file_path, 'w') as file:
        file.write(markdown_table)

    df.to_csv(f'{name}.csv', index=False)

# Data frames
data1 , data2 = excuteAgents()
df1 = convertirDfs(data1)
df2 = convertirDfs(data2)

#Exportamos los datos en csv
export_dataframes('ReflexiveAgentData',df1)
export_dataframes('RandomAgentData',df2)



















'''
def executeReflexiveAgent():
    x = ['Agente 2x2' , 'Agente 4x4' , 'Agente 8x8' , 'Agente 16x16' , 'Agente 32x32' , 'Agente 64x64', 'Agente 128x128']
    j = 0
    datos = {'Agente 2x2' : [] , 'Agente 4x4' : [] , 'Agente 8x8' : [] , 'Agente 16x16' : [], 'Agente 32x32': [] , 
             'Agente 64x64': [], 'Agente 128x128' : []}
    cantidad_entornos = 7
    dirt_rates = [0.1,0.2,0.4,0.8]
    tamano = 2
    for i in range(cantidad_entornos):
        for k in range(len(dirt_rates)):
            for j in range(10):
                agent = ReflexiveAgent(Environment(tamano,tamano,random.randint(0,tamano-1),random.randint(0,tamano-1),dirt_rates[k]))
                result = executeAgent(agent,agent.env,'Reflexivo ' + x[i],j)
                result.append(dirt_rates[k])
                datos[x[i]].append(result)
        tamano *= 2
    return datos

def excuteRandomAgent():
    x = ['Agente 2x2' , 'Agente 4x4' , 'Agente 8x8' , 'Agente 16x16' , 'Agente 32x32' , 'Agente 64x64', 'Agente 128x128']
    j = 0
    datos = {'Agente 2x2' : [] , 'Agente 4x4' : [] , 'Agente 8x8' : [] , 'Agente 16x16' : [], 'Agente 32x32': [] , 
             'Agente 64x64': [], 'Agente 128x128' : []}
    cantidad_entornos = 7
    dirt_rates = [0.1,0.2,0.4,0.8]
    tamano = 2
    for i in range(cantidad_entornos):
        for k in range(len(dirt_rates)):
            for j in range(10):
                agent = RandomAgent(Environment(tamano,tamano,0,0,dirt_rates[k]))
                result = executeAgent(agent,agent.env,'Aleatorio ' +x[i],j)
                result.append(dirt_rates[k])
                datos[x[i]].append(result)
        tamano *= 2
    return datos



'''
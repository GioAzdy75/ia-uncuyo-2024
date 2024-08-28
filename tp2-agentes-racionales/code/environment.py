import random
import math

class Environment:
    @staticmethod
    def dirtyGrid(array,x,y,dirt_rate):
        z = math.ceil(x*y*dirt_rate)
        for _ in range(z):
            array[random.randint(0,x-1)][random.randint(0,y-1)] = 1
        return array
    def __init__(self,sizeX:int,sizeY:int,init_posX:int,init_posY:int,dirt_rate:float):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.init_posX = init_posX
        self.init_posY = init_posY
        self.dirt_rate = dirt_rate
        self.grid = Environment.dirtyGrid([[0 for _ in range(sizeY)] for _ in range(sizeX)],sizeX,sizeY,dirt_rate)
        self.performance = 0
        self.movpoints = 0
        self.list_movpoints = []
        
    def accept_action(self,action):
        if (action == 'Arriba'):
            if (self.init_posY < len(self.grid)-1):
                self.init_posY = self.init_posY + 1
                self.movpoints +=1
        elif (action == 'Abajo'):
            if (self.init_posY > 0):
                self.init_posY = self.init_posY - 1
                self.movpoints +=1
        elif (action == 'Izquierda'):
            if (self.init_posX > 0):
                self.init_posX = self.init_posX - 1
                self.movpoints +=1
        elif (action == 'Derecha'):
            if (self.init_posX < len(self.grid)-1):
                self.init_posX = self.init_posX + 1
                self.movpoints +=1
        elif (action == 'Limpiar'):
            #Arrglar codigo ()
            #self.grid[self.init_posX][self.init_posY] = 0
            #self.performance += 1
            if self.is_dirty():
                self.grid[self.init_posX][self.init_posY] = 0
                self.performance += 1
                self.list_movpoints.append(self.movpoints)
                self.movpoints = 0

    def is_dirty(self):
        return self.grid[self.init_posX][self.init_posY] > 0
    
    def get_performance(self):
        return self.performance

    def print_environment(self):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                print('|' + str(self.grid[i][j]) + '|',end=" ")
            print()
        print('---------')
from environment import Environment
import random

class Agent:
    def __init__(self,env:Environment): # recibe como parametro un objeto de la clase Environment
        self.env = env
        self.actions = [self.up,self.down,self.left,self.right,self.suck,self.idle]
        self.life = 1000

    def decrease_life(self,i):
        self.life -= i
        if (self.life < 0) : 
            self.life = 0

    def up(self):
        self.env.accept_action('Arriba')
        self.decrease_life(1)
    def down(self):
        self.env.accept_action('Abajo')
        self.decrease_life(1)
    def left(self):
        self.env.accept_action('Izquierda')
        self.decrease_life(1)
    def right(self):
        self.env.accept_action('Derecha')
        self.decrease_life(1)
    def suck(self): # Limpia
        self.env.accept_action('Limpiar')
        self.decrease_life(1)

    def idle(self): # no hace nada
        pass

    def isdirty(self):
        return self.env.is_dirty()
    
    def get_performance(self):
        return self.env.get_performance()

    def perspective(self,env): # sensa el entorno
        pass

    def think(self): # implementa las acciones a seguir por el agente
        pass


class ReflexiveAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)
        self.actions = [self.up,self.down,self.left,self.right]

    def think(self):
        if (self.isdirty()):
            self.suck()
            random.choice(self.actions)()
        else:
            random.choice(self.actions)()

class RandomAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)

    def think(self):
        random.choice(self.actions)()
import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
        # lista que contiene la posición inicial

    def make_move(self):

        # Selecciona un movimiento aleatorio de la lista de movimientos disponibles
        move = random.choice(self.moves)
        # Sumo componentes cartesianas del movimiento a la posición actual
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
            # alternativamente podría haber usado self.position += (move[0], move[1])

        self.path.append(self.position)   
        # Agrega la nueva posición a la lista de posiciones recorridas     
        return (self.position)

    @abstractmethod
    def level_up(self):
        pass     

class Pawn(Player):
    def __init__(self):
        super().__init__()

        self.moves=[(0,1),(0,-1),(-1,0),(1,0)] 
        # arriba, abajo, izquierda, derecha
    
    def level_up(self):

        self.moves.extend([(1,1),(-1,1),(-1,-1),(1,-1)])
        # diagonales
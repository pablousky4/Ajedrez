import random
import math

class ProblemaCaballo:
    def __init__(self, N=8):
        self.N = N 
        self.movimientos_caballo = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        self.tablero = [[-1 for _ in range(N)] for _ in range(N)]
        self.recorrido = []  

    def es_valido(self, x, y):
        print("wewewe")
        return 0 <= x < self.N and 0 <= y < self.N and self.tablero[x][y] == -1

    def resolver_caballo(self, x, y, paso):
        print("wewewe")
        self.tablero[x][y] = paso  
        self.recorrido.append((x, y)) 

        if paso == self.N * self.N - 1:
            return True  

        for dx, dy in self.movimientos_caballo:
            nx, ny = x + dx, y + dy
            if self.es_valido(nx, ny):
                if self.resolver_caballo(nx, ny, paso + 1):
                    return True
        self.tablero[x][y] = -1
        self.recorrido.pop()
        return False

    def resolver(self, inicio_x=0, inicio_y=0):
        if self.resolver_caballo(inicio_x, inicio_y, 0):
            print("wewewe")
            return self.tablero
        else:
            print("No se encontró solución.")
            return None
from caballo.caballo import ProblemaCaballo
import random

class CaballoConRecorrido(ProblemaCaballo):
    def __init__(self, N=8):
        super().__init__(N)
        self.recorrido = []  

    def resolver_caballo(self, x, y, paso):
        if paso == self.N * self.N:
            self.recorrido.append((x, y)) 
            return True  

        for dx, dy in self.movimientos_caballo:
            nx, ny = x + dx, y + dy
            if self.es_valido(nx, ny):
                self.tablero[nx][ny] = paso  
                self.recorrido.append((x, y))  
                if self.resolver_caballo(nx, ny, paso + 1):
                    return True
                self.tablero[nx][ny] = -1 
                self.recorrido.pop()  

        return False

    def obtener_recorrido(self):
        return self.recorrido

if __name__ == "__main__":
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    caballo = CaballoConRecorrido()
    solucion = caballo.resolver(inicio_x, inicio_y)

    if solucion:
        print("¡El caballo visitó todas las casillas!")
        print("Recorrido del caballo:")
        for paso, posicion in enumerate(caballo.obtener_recorrido()):
            print(f"Paso {paso + 1}: {posicion}")
        print("\nTablero final:")
        caballo.imprimir_tablero()
    else:
        print("No se encontró una solución para el recorrido del caballo.")
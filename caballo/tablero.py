from caballo.caballo import ProblemaCaballo

class TableroVisual:
    def __init__(self, N=8):
        self.N = N
        self.problema_caballo = ProblemaCaballo(N)

    def convertir_a_notacion_ajedrez(self, x, y):
        columnas = "abcdefgh"
        return f"{columnas[y]}{self.N - x}"

    def mostrar_tablero(self, tablero):
        print("Recorrido del caballo en el tablero:")
        print("   " + " ".join("abcdefgh"))  
        for i, fila in enumerate(tablero):
            print(f"{self.N - i} | " + " ".join(f"{celda:2}" if celda != -1 else " ." for celda in fila))
        print("   " + " ".join("abcdefgh")) 

    def guardar_recorrido(self, recorrido):
        movimientos_ajedrez = []
        vector_recorrido = []

        for x, y in recorrido:
            movimientos_ajedrez.append(self.convertir_a_notacion_ajedrez(x, y))
            vector_recorrido.append((x, y))

        with open("movimientos.txt", "w") as f:
            f.write(" -> ".join(movimientos_ajedrez))

        with open("vector.txt", "w") as f:
            f.write(str(vector_recorrido))

        print("\nGuardado en:")
        print("- movimientos.txt ")
        print("- vector.txt ")

    def ejecutar(self, inicio_x=0, inicio_y=0):
        solucion = self.problema_caballo.resolver(inicio_x, inicio_y)
        if solucion:
            self.mostrar_tablero(self.problema_caballo.tablero)
            self.guardar_recorrido(self.problema_caballo.recorrido)
        else:
            print("No se encontró una solución.")
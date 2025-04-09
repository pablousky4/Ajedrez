class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.palos = {
            "A": list(range(num_discos, 0, -1)),  
            "B": [], 
            "C": []  
        }
        self.movimientos = []

    def mover_disco(self, origen, destino):
        disco = self.palos[origen].pop()
        self.palos[destino].append(disco)
        self.movimientos.append(f"Se mueve {disco} de {origen} a {destino}")
        self.mostrar_palos()

    def resolver(self, num_discos=None, origen="A", auxiliar="B", destino="C"):
        if num_discos is None:
            num_discos = self.num_discos

        if num_discos == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(num_discos - 1, origen, destino, auxiliar)
            self.mover_disco(origen, destino)
            self.resolver(num_discos - 1, auxiliar, origen, destino)

    def mostrar_palos(self):
        print("\nEstado de los palos:")
        for palo, discos in self.palos.items():
            print(f"{palo}: {discos}")

    def imprimir_movimientos(self):
        print("\nMovimientos necesarios para resolver la Torre de Hanoi:")
        for paso, movimiento in enumerate(self.movimientos, start=1):
            print(f"Paso {paso}: {movimiento}")
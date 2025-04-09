from caballo.tablero import TableroVisual
from reina.reina import resolver_reina
#from hanoi.hanoi import TorreDeHanoi
import random

def juego_de_caballo():
    print("Ejecutando Caballo")
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)

def juego_de_reinas():
    print("Ejecutando Reina")
    N = int(input("Tamaño tablero (N): "))
    soluciones = resolver_reina(N)
    with open("reina.txt", "w") as archivo:
        for solucion in soluciones:
            archivo.write(f"{solucion}\n")
    print("Soluciones guardadas en 'reina.txt'.")


if __name__ == "__main__":
    while True:
        print("\nSeleccione una opción:")
        print("1. Caballo")
        print("2. Reinas")
        print("3. Torre de Hanoi")
        print("4. Salir")
        opcion = input("Ingrese el número de su elección: ")

        if opcion.isdigit():
            if opcion == "1":
                juego_de_caballo()
            elif opcion == "2":
                juego_de_reinas()
            elif opcion == "3":
                pass
                #problema_de_hanoi()
            elif opcion == "4":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        else:
            print("Por favor, ingrese un número válido.")
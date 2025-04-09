from caballo.tablero import TableroVisual
import random

def juego_de_caballo():
    print("¡Bienvenido al problema del caballo!")
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición 1 del caballo: ({inicio_x}, {inicio_y})")
    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)


if __name__ == "__main__":
    while True:
        print("\nSelecciona el juego:")
        print("1. Caballo")
        #print("2. Reinas")
        #print("3. Torre de Hanoi")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion.isdigit():
            if opcion == "1":
                juego_de_caballo()
            elif opcion == "4":
                print("salir")
                break
            else:
                print("Incorrecto")
        else:
            print("Incorrecto")
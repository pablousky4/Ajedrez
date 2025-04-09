from caballo.caballo import generar_tabla_movimientos
from reina.reina import resolver_reina
from hanoi.hanoi import TorreDeHanoi

def juego_de_caballo():
    print("Ejecutando Caballo")
    generar_tabla_movimientos()
    print("Archivo 'movimientos.txt' generado correctamente.")


def juego_de_reinas():
    print("Ejecutando Reina")
    N = int(input("Tamaño tablero (N): "))
    soluciones = resolver_reina(N)
    with open("reina.txt", "w") as archivo:
        for solucion in soluciones:
            archivo.write(f"{solucion}\n")
    print("Soluciones guardadas en 'reina.txt'.")

def problema_de_hanoi():
    print("¡Bienvenido al problema de la Torre de Hanoi!")
    num_discos = int(input("Ingrese el número de discos: "))
    hanoi = TorreDeHanoi(num_discos)
    print("\nEstado inicial de los palos:")
    hanoi.mostrar_palos()
    hanoi.resolver()
    hanoi.imprimir_movimientos()

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
                problema_de_hanoi()
            elif opcion == "4":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        else:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

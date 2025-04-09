def contar_movimientos_validos(n):
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    dp = [1] * 10
    for _ in range(n):
        new_dp = [0] * 10
        for i in range(10):
            for j in moves[i]:
                new_dp[i] += dp[j]
        dp = new_dp

    return sum(dp)


def generar_tabla_movimientos(nombre_archivo="movimientos.txt"):
    movimientos = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Cantidad de movimientos | Posibilidades válidas\n")
        archivo.write("-----------------------------------------------\n")
        for m in movimientos:
            total = contar_movimientos_validos(m)
            archivo.write(f"{m:<23} | {total}\n")

    print(f"Archivo '{nombre_archivo}' guardado correctamente.")


if __name__ == "__main__":
    generar_tabla_movimientos()

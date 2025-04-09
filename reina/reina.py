def resolver_reina(N):
    soluciones = []
    tablero = [-1] * N  

    def es_valido(fila, columna):
        for i in range(fila):
            if tablero[i] == columna or abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def volver(fila):
        if fila == N:
            soluciones.append(tablero[:])
            return
        for columna in range(N):
            if es_valido(fila, columna):
                tablero[fila] = columna
                volver(fila + 1)
                tablero[fila] = -1  
    volver(0)
    return soluciones
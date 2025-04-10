import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resolver_n_reinas(n):

    def es_seguro(tablero, fila, columna):
        for i in range(columna):
            if tablero[i] == fila or \
               tablero[i] - i == fila - columna or \
               tablero[i] + i == fila + columna:
                return False
        return True

    def resolver(columna, tablero, soluciones):
        if columna == n:
            soluciones.append(tablero[:])
            return
        for fila in range(n):
            if es_seguro(tablero, fila, columna):
                tablero[columna] = fila
                resolver(columna + 1, tablero, soluciones)

    soluciones = []
    resolver(0, [-1] * n, soluciones)
    return soluciones

def mostrar_resultado_reinas():
    n = int(entrada_reinas.get())
    ruta_imagen = f"images/n_queens_{n}.png"
    try:
        img = Image.open(ruta_imagen)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        etiqueta_imagen.config(image=img_tk)
        etiqueta_imagen.image = img_tk
    except FileNotFoundError:
        etiqueta_imagen.config(text=f"No se encontró la imagen en '{ruta_imagen}'.")

raiz = tk.Tk()
raiz.title("Resolver N-Reinas")

ttk.Label(raiz, text="Número de reinas:").grid(row=0, column=0, padx=5, pady=5)
entrada_reinas = ttk.Entry(raiz)
entrada_reinas.grid(row=0, column=1, padx=5, pady=5)
entrada_reinas.insert(0, "4")

boton_calcular = ttk.Button(raiz, text="Mostrar solución", command=mostrar_resultado_reinas)
boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)

etiqueta_imagen = ttk.Label(raiz)
etiqueta_imagen.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

raiz.mainloop()

